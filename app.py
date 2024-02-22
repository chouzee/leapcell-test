from flask import Flask, render_template, request, redirect, url_for
import os
import markdown
import datetime
import time
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)

@app.route("/")
def index():
    return 'h'



if __name__ == "__main__":
    app.run(debug=True)
