#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect

import settings
import members

app = Flask(__name__)
app.debug = False

@app.route('/')
def home():
    return render_template('home.html', menus=settings.MENUS,
            dirlinks=settings.DIRLINKS, active_page='Home')

@app.route('/blog')
def blog():
    return redirect('http://blog.popong.com')

@app.route('/about')
def about():
    return render_template('about.html', menus=settings.MENUS,
            dirlinks=settings.DIRLINKS, active_page='About')

@app.route('/error')
def error():
    return 'error ;_;'

def main():
    app.run(**settings.SERVER_SETTINGS)

if __name__ == '__main__':
    main()
