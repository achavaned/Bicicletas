from flask import Flask, jsonify, request, render_template, redirect, url_for
from bson import json_util, ObjectId
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=8001)