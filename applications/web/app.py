#!/usr/bin/env python3
"""
Basic entry into the Denver Concerts web application
"""

from flask import Flask, request
from applications.web.htmlhelper import HtmlHelper

app = Flask(__name__)
htmlHelper = HtmlHelper()


@app.route("/")
def main() -> str:
    """ Route: Web Application Homepage """
    return htmlHelper.get_header(title='User Input') + '''
    <form action="/display-user-input" method="POST" style="display: flex; flex-direction: column; margin-block-end: 0;">
        <label for="user_feeling" style="font-size: 24px; margin-bottom: 16px; font-family: sans-serif;">👋 How are you feeling today?</label>
        <input type="text" name="user_feeling" id="user_feeling" placeholder="Good, bad, ready to rock, etc..." style="height: 36px; border-radius 40px; padding: 10px 20px; font-size: 24px;" />
        <input type="submit" value="✉️ SUBMIT" style="background: #080808; color: #fff; margin-top: 16px; height: 36px; border-radius: 40px; text-align: center; font-size: 24px; border: none;" />
     </form>
    ''' + htmlHelper.get_footer()


@app.route("/display-user-input", methods=["POST"])
def echo_unput() -> str:
    """ Route: After User Input """
    input_text = request.form.get("user_feeling", "")
    if not input_text:
        input_text = "Nothing 😢"
    return htmlHelper.get_header(title='Response') + f'''
        <p style="font-size: 18px; margin-bottom: 16px; font-family: sans-serif; text-align: center; color: #666;">
            🔊 You said:
        </p>
        <p style="font-size: 24px; margin-bottom: 16px; font-family: sans-serif; text-align: center;">
            {input_text}
        </p>
        <p style="font-size: 18px; margin-bottom: 16px; font-family: sans-serif; text-align: center; color: #666;">
            👨‍🔧 Check back for an easier way to find <em>good</em> concerts in Denver, CO.
        </p>
        <p style="text-align: center;"><a href="/">Try Again</a>
    ''' + htmlHelper.get_footer()
