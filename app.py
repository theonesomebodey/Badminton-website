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
        # Use eval to calculate the answer, careful with user input here, but these are controlled numbers
        answer = eval(question_str)
    except ZeroDivisionError: # Avoid division by zero if we ever add '/'
        return generate_math_question() # Regenerate if division by zero occurs
    
    # Store the question string and its correct answer in the session
    session['math_question'] = question_str
    session['math_answer'] = answer
    return question_str


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/signup.html', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':

        user_math_answer = request.form.get('math_answer_input')
        correct_math_answer = session.get('math_answer')

        # --- 2. Validate Math Answer ---
        if not user_math_answer or str(user_math_answer) != str(correct_math_answer):
            flash('Incorrect math answer. Please try again.', 'error')
            # Clear session math values to force new question
            session.pop('math_question', None)
            session.pop('math_answer', None)
            return redirect(url_for('signup')) # Redirect to GET request to show new question

        # --- Clear math session values after successful validation ---
        session.pop('math_question', None)
        session.pop('math_answer', None)
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
        messagetoplayer = (
            f"Thank You For Signing Up🎉{fullname}\n"
            f"We are excited to see you compete on August 2nd!"
        )
        msg = MIMEText(messagetoplayer)
        msg['From'] = 'shawnxionggg@gmail.com'
        msg['To'] = email
        msg['Subject'] = "Thank You!" + fullname
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('shawnxionggg@gmail.com', password)
        server.send_message(msg)
        server.quit()


        msg = MIMEText(message)
        msg['From'] = 'shawnxionggg@gmail.com'
        msg['To'] = 'shawnxionggg@gmail.com'
        msg['Subject'] = "player - " + fullname
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('shawnxionggg@gmail.com', password)
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

        # --- 2. Validate Math Answer ---
        if not user_math_answer or str(user_math_answer) != str(correct_math_answer):
            flash('Incorrect math answer. Please try again.', 'error')
            # Clear session math values to force new question
            session.pop('math_question', None)
            session.pop('math_answer', None)
            return redirect(url_for('volunteer')) # Redirect to GET request to show new question

        # --- Clear math session values after successful validation ---
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
        messagetovolunteer = (
            f"Thank You {fullname}\n"
            f"We are excited to see you on August 2nd!"
        )
        msg = MIMEText(messagetovolunteer)
        msg['From'] = 'shawnxionggg@gmail.com'
        msg['To'] = email
        msg['Subject'] = "Thank You!" + fullname
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('shawnxionggg@gmail.com', password)
        server.send_message(msg)
        server.quit()


        msg = MIMEText(message)
        msg['From'] = 'shawnxionggg@gmail.com'
        msg['To'] = 'shawnxionggg@gmail.com'
        msg['Subject'] = "volunteer - " + fullname
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('shawnxionggg@gmail.com', password)
        server.send_message(msg)
        server.quit()
        return render_template('thankyouvolunteer.html')
    else:
        math_question_str = generate_math_question()
        return render_template('volunteer.html', math_question=math_question_str)
    


    
    

    
    
