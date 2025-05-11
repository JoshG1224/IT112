from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Setup SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Game model
class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    platform = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Game {self.title}>"

# Create DB and seed data if empty
with app.app_context():
    db.create_all()
    if Game.query.count() == 0:
        games = [
            Game(title="The Legend of Zelda", genre="Adventure", platform="Nintendo"),
            Game(title="Halo", genre="Shooter", platform="Xbox"),
            Game(title="Minecraft", genre="Sandbox", platform="PC"),
            Game(title="Final Fantasy", genre="RPG", platform="PlayStation")
        ]
        db.session.add_all(games)
        db.session.commit()

# Home page
@app.route("/")
def home():
    return render_template('home.html')

# About page
@app.route("/about")
def about():
    return render_template('about.html')

# Fortune route
@app.route("/fortune", methods=["GET", "POST"])
def fortune():
    if request.method == "POST":
        name = request.form["user"]
        color = request.form["color"]
        number = request.form["number"]
        fortunes = {
            ('red', '1'): "Today is your lucky day!",
            ('red', '2'): "Watch out for unexpected surprises.",
            ('yellow', '3'): "Success is on the horizon.",
            ('blue', '4'): "A new friendship is forming.",
            ('green', '5'): "Trust your instincts today.",
        }
        fortune_result = fortunes.get((color, number), "Your future holds great potential.")
        return f"<h2>{name}, your fortune is: {fortune_result}</h2>"
    return render_template('fortune.html')

# Show all games
@app.route("/games")
def games():
    all_games = Game.query.all()
    return render_template('games.html', games=all_games)

# Game detail view
@app.route("/games/<int:game_id>")
def game_detail(game_id):
    game = Game.query.get_or_404(game_id)
    return render_template("game_detail.html", game=game)

# Combined GET + POST API route for games
@app.route("/api/games", methods=["GET", "POST"])
def api_games():
    if request.method == "GET":
        games = Game.query.all()
        games_list = [
            {"id": g.id, "title": g.title, "genre": g.genre, "platform": g.platform}
            for g in games
        ]
        return jsonify(games_list), 200

    elif request.method == "POST":
        try:
            data = request.get_json()
            title = data["title"]
            genre = data["genre"]
            platform = data["platform"]
            new_game = Game(title=title, genre=genre, platform=platform)
            db.session.add(new_game)
            db.session.commit()
            return jsonify({"message": "Game added successfully!"}), 200
        except Exception as e:
            print("Error adding game:", e)
            return jsonify({"error": "Failed to add game"}), 500

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

