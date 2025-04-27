from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Setup Flask app
app = Flask(__name__)

# Setup database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.db'
db = SQLAlchemy(app)

# Define the database model
class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    platform = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Game {self.title}>
'''
# Create the database tables (ONLY RUN ONCE)
with app.app_context():
    db.create_all()

    # OPTIONAL: Add games ONLY if db is empty
    if Game.query.count() == 0:
        game1 = Game(title="The Legend of Zelda", genre="Adventure", platform="Nintendo")
        game2 = Game(title="Halo", genre="Shooter", platform="Xbox")
        game3 = Game(title="Minecraft", genre="Sandbox", platform="PC")
        game4 = Game(title="Final Fantasy", genre="RPG", platform="PlayStation")
        db.session.add_all([game1, game2, game3, game4])
        db.session.commit()
'''
# ROUTES

@app.route("/")
def home():
    return render_template('home.html')  # your home template

@app.route("/about")
def about():
    return render_template('about.html')  # your about template

@app.route('/fortune', methods=['GET', 'POST'])
def fortune():
    if request.method == 'POST':
        name = request.form['user']
        color = request.form['color']
        number = request.form['number']
        fortunes = {
            ('red', '1'): "Today is your lucky day!",
            ('red', '2'): "Watch out for unexpected surprises.",
            ('yellow', '3'): "Success is on the horizon.",
            ('blue', '4'): "A new friendship is forming.",
            ('green', '5'): "Trust your instincts today.",
        }
        fortune_result = fortunes.get((color, number), "Your future holds great potential.")
        return f"<h2>{name}, your fortune is: {fortune_result}</h2>"

    return render_template('fortune.html')  # Move the form to fortune.html

# Show all games
@app.route('/games')
def games():
    all_games = Game.query.all()
    return render_template('games.html', games=all_games)

# Detail page for a single game
@app.route('/games/<int:game_id>')
def game_detail(game_id):
    game = Game.query.get_or_404(game_id)
    return render_template('game_detail.html', game=game)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
