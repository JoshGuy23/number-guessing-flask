from flask import Flask
import random

app = Flask(__name__)

answer = random.randint(0, 9)


@app.route("/<int:num>")
def guess_page(num: int):
    if num == answer:
        html = ('<h1 style="color:green">You found me!</h1>'
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" '
                'alt="A puppy popping out of a cookie tin."/>')
    elif num < answer:
        html = ('<h1 style="color:red">Too low, try again!</h1>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" '
                'alt="A puppy trying and failing to dig dirt at the base of a tree, '
                'then slumping down in defeat."/>')
    else:
        html = ('<h1 style="color:purple">Too high, try again!</h1>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" '
                'alt="A puppy flailing its arms while being carried."/>')
    return html


@app.route("/")
def home_page():
    html = ('<h1>Guess a Number between 0 and 9</h1>'
            '<p>Enter your guess at the end of the url after a slash.</p>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" '
            'alt="Gif of various numbers rapidly appearing"/>')
    return html


if __name__ == "__main__":
    app.run(debug=True)
