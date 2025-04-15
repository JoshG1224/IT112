from flask import Flask

app = Flask(__name__)

# Default route
@app.route('/')
def home():
    return "<h1>My Flask Application</h1>"

# About route
@app.route('/about')
def about():
    return "<p>Hello, I'm Josh, and this is my Flask app for class.</p>"

if __name__ == '__main__':
    app.run(debug=True)
