#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])

def index():
    message = None
    db = MongoDB(app)
    message = db.get_data()
    return render_template('index.html', message=message)

if  __name__ == '__main__':
    app.run()

