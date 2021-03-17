from flask import Blueprint, render_template

ttt = Blueprint("ttt", __name__)

ttt.route("/tictactoe")
def tictactoe():
    return '<h1><center>Tic Tac Toe Game</center></h1>'
