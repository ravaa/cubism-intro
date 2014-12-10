#!/usr/bin/env python
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('03.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
