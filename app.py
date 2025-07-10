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
        events = request.form.getlist('events') # For multiple checkboxes
        partner_name = request.form.get('partnerName') # Will be None if not visible/filled

        message = (
            f"**New Player Form Submission:**\n"
            f"**Full Name:** {fullname}\n"
            f"**Email:** {email}\n"
            f"**Phone:** {phone}\n"
            f"**Skill Level:** {skillLevel}\n"
            f"**Events Selected:** {', '.join(events)}\n"
            f"**Partner Name:** {partner_name}\n"
        )


        msg = MIMEText(message)
        msg['From'] = 'shawnxionggg@gmail.com'
        msg['To'] = 'shawnxionggg@gmail.com'
        msg['Subject'] = "player - " + fullname
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

        message = (
            f"**New Volunteer Form Submission:**\n"
            f"**Full Name:** {fullname}\n"
            f"**Email:** {email}\n"
            f"**Phone:** {phone}\n"
        )


        msg = MIMEText(message)
        msg['From'] = 'shawnxionggg@gmail.com'
        msg['To'] = 'shawnxionggg@gmail.com'
        msg['Subject'] = "volunteer - " + fullname
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('shawnxionggg@gmail.com', 'mwbp njni qlfo vfqf')
        server.send_message(msg)
        server.quit()
        return render_template('thankyouvolunteer.html')
    else:
        return render_template('volunteer.html')
    



    
    
