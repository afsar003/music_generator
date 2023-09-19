from flask import Flask, render_template
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)

logging.basicConfig(level = logging.ERROR)

@app.route("/")
def first_page():
    return render_template("firstpage.html")

@app.route("/music_player")
def second_page():
    return render_template("music_player.html")

if __name__ == "__main__":
    try:
        app.run(debug=True, host = "0.0.0.0", port = 5000)
    except:
        print("Keyboard Interrupt: logging off...")