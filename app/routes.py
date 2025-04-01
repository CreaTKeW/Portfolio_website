from flask import render_template, current_app as app

@app.route('/')
def home_route():
    return "<h1>Home Page!</h1>"

@app.route('/portfolio')
def portfolio():
    return "<h1>Portfolio</h1>"

@app.route('/contact')
def contact():
    return "<h1>Contact</h1>"