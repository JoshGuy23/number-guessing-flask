from flask import Flask

app = Flask(__name__)


@app.route("/")
def home_page():
    html = ('<h1>Guess a Number between 0 and 9</h1>'
            '<p>Enter your guess at the end of the url.</p>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" '
            'alt="Gif of various numbers rapidly appearing"/>')
    return html


if __name__ == "__main__":
    app.run(debug=True)
