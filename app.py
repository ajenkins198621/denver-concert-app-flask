#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def main() -> str:
    return '''
    <form action="/echo-user-input" method="POST">
        <input type="text" name="user_input" />
        <input type="submit" value="Submit!" />
     </form>
    '''


@app.route("/echo-user-input", methods=["POST"])
def echo_unput() -> str:
    input_text = request.form.get("user_input", "")
    return "You entered: " + input_text
