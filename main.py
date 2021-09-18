#!/usr/bin/python
# -*- coding: Utf-8 -*-

from datetime import datetime
from flask import Flask, render_template, request, redirect, session
import os


app = Flask(__name__,
    template_folder=os.path.abspath('html/'))

app.secret_key = "ahcestcontulaspas"
app.debug = True




@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login')
def login():
    return render_template("login.html")



if __name__ == '__main__':
    app.run()
