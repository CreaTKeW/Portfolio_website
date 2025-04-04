import datetime
from flask import render_template, redirect, url_for, flash, current_app as app
from app.forms import ContactForm


@app.context_processor
def inject_current_year():
    return {'current_year': datetime.datetime.now().year}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():

        name = form.name.data
        email = form.email.data
        phone = form.phone.data
        message = form.message.data

        print(f"Wiadomość od: {name} ({email}), Tel: {phone}")
        print(f"Treść: {message}")

        flash('Your message has been successfully sent.', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html', form=form)