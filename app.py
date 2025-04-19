from flask import Flask, request, render_template

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return render_template("home.html")

# About route
@app.route("/about")
def about():
    return render_template("about.html")

# Fortune route
@app.route("/fortune", methods=["GET", "POST"])
def fortune():
    if request.method == "POST":
        name = request.form["user"]
        color = request.form["color"]
        number = request.form["number"]

        fortunes = {
            ("red", "1"): "Today is your lucky day!",
            ("red", "2"): "Watch out for unexpected surprises.",
            ("yellow", "3"): "Success is on the horizon.",
            ("blue", "4"): "A new friendship is forming.",
            ("green", "5"): "Trust your instincts today.",
        }

        fortune_result = fortunes.get((color, number), "Your future holds great potential.")
        return render_template("fortune.html", name=name, fortune=fortune_result)

    return render_template("fortune.html")


if __name__ == "__main__":
    app.run(debug=True)
