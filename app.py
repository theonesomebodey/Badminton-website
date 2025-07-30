from flask import Flask, render_template, request, session, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText
import os
import random
password = os.getenv('password')

app = Flask(__name__)

app.secret_key = os.getenv('password2')
def generate_math_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operators = ['+', '-', '*']
    operator = random.choice(operators)

    question_str = f"{num1} {operator} {num2}"
    try:
        answer = eval(question_str)
    except ZeroDivisionError:
        return generate_math_question() 
    
    session['math_question'] = question_str
    session['math_answer'] = answer
    return question_str


@app.route('/')
def main():
    return render_template('main.html')
@app.route('/donate.html') 
def donate():
    return render_template('donate.html')

@app.route('/signup.html', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':

        user_math_answer = request.form.get('math_answer_input')
        correct_math_answer = session.get('math_answer')

        if not user_math_answer or str(user_math_answer) != str(correct_math_answer):
            flash('Incorrect math answer. Please try again.', 'error')
            session.pop('math_question', None)
            session.pop('math_answer', None)
            return redirect(url_for('signup'))

        session.pop('math_question', None)
        session.pop('math_answer', None)
        fullname = request.form.get('fullName')
        email = request.form.get('email')
        phone = request.form.get('phone')
        skillLevel = request.form.get('skillLevel')
        events = request.form.getlist('events') 
        partner_name = request.form.get('partnerName') 

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
        msg['From'] = 'juniorflybear@gmail.com'
        msg['To'] = 'juniorflybear@gmail.com'
        msg['Subject'] = "player - " + fullname
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('juniorflybear@gmail.com', password)
        server.send_message(msg)
        server.quit()
        return render_template('thankyou.html')
    else:
        math_question_str = generate_math_question()
        return render_template('signup.html', math_question=math_question_str)
    
@app.route('/volunteer.html', methods=['GET', 'POST'])
def volunteer():
    if request.method == 'POST':


        user_math_answer = request.form.get('math_answer_input')
        correct_math_answer = session.get('math_answer')


        if not user_math_answer or str(user_math_answer) != str(correct_math_answer):
            flash('Incorrect math answer. Please try again.', 'error')

            session.pop('math_question', None)
            session.pop('math_answer', None)
            return redirect(url_for('volunteer')) 
        session.pop('math_question', None)
        session.pop('math_answer', None)

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
        msg['From'] = 'juniorflybear@gmail.com'
        msg['To'] = 'juniorflybear@gmail.com'
        msg['Subject'] = "volunteer - " + fullname
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('juniorflybear@gmail.com', password)
        server.send_message(msg)
        server.quit()
        return render_template('thankyouvolunteer.html')
    else:
        math_question_str = generate_math_question()
        return render_template('volunteer.html', math_question=math_question_str)
    


    
    

    
    
