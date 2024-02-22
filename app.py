from flask import Flask, render_template, request, redirect, url_for
from leapcell import Leapcell
import os
import markdown
import datetime
import time
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)

api = Leapcell(
    api_key=os.environ.get("LEAPCELL_API_KEY"),
)



@app.route("/")
def index():
    return 'Hello'



if __name__ == "__main__":
    app.run(debug=True)
