import datetime
import os
from flask import render_template, redirect, url_for, flash, current_app as app
from app.forms import ContactForm
from flask_mail import Message
from app import mail


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

        recipient_email = os.getenv('MAIL_RECIPIENT') or app.config['MAIL_DEFAULT_SENDER']

        try:
            msg = Message(
                subject=f"New message from: {name}",
                sender=app.config['MAIL_DEFAULT_SENDER'],
                recipients=[recipient_email],
                reply_to=email
            )
            msg.body = f"""
                   Recived a new message from contact form:

                   From: {name}
                   Email: {email}
                   Phone number: {phone if phone else 'Not provided'}

                   Message:
                   {message}
                   """

            mail.send(msg)

            flash('Your message has been successfully sent!', 'success')

        except Exception as e:
            app.logger.error(f"Error while sending a message: {e}")
            flash('Error has occurred while trying to send a message. Try again later.', 'danger')

        return redirect(url_for('contact'))
    return render_template('contact.html', form=form)