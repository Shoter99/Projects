from flask import Flask, request, url_for, redirect, render_template


app = Flask(__name__)

@app.route("/")
def home():
    return "<center><h1>Welcome on Iland Website</h1><br><h3>Take a look around</h3></center>"


if __name__ == "__main__":
    app.run(debug=True)