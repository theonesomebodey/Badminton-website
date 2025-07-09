from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/signup.html', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        fullname = request.form.get('fullName')
        email = request.form.get('email')
        phone = request.form.get('phone')
        skillLevel = request.form.get('skillLevel')
        msg = MIMEText(fullname + email + phone + skillLevel)
        msg['From'] = 'shawnxionggg@gmail.com'
        msg['To'] = 'shawnxionggg@gmail.com'
        msg['Subject'] = "some 1 signed up"
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('shawnxionggg@gmail.com', 'mwbp njni qlfo vfqf')
        server.send_message(msg)
        server.quit()
        return render_template('thankyou.html')
    else:
        return render_template('signup.html')
    
@app.route('/volunteer.html', methods=['GET', 'POST'])
def volunteer():
    if request.method == 'POST':
        fullname = request.form.get('fullName')
        email = request.form.get('email')
        phone = request.form.get('phone')
        msg = MIMEText(fullname + email + phone)
        msg['From'] = 'shawnxionggg@gmail.com'
        msg['To'] = 'shawnxionggg@gmail.com'
        msg['Subject'] = "some 1 signed up"
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('shawnxionggg@gmail.com', 'mwbp njni qlfo vfqf')
        server.send_message(msg)
        server.quit()
        return render_template('thankyouvolunteer.html')
    else:
        return render_template('volunteer.html')
    
    
