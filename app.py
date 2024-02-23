from flask import Flask, render_template, request, redirect, url_for, jsonify
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
    return 'home'

@app.route("/api")
def api():
    return jsonify({"привіт": "hello", "бувай": "goodbye"})

if __name__ == "__main__":
    app.run(debug=True)
