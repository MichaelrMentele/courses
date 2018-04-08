from flask import Flask, jsonify


app = Flask(__name__)

"""
This flask app every ~10 seconds selects a new 'favorite' book from a
list. It then stores this favorite book and multicasts it to all of it's
known peers.
"""


@app.route('/pong')
def pongable():
    return 'PONG'


if __name__ == "__main__":
    app.run()
