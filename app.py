from flask import Flask, render_template, request, redirect, url_for, flash


volunteers = "volunteers.txt"
players = "players.txt"
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
        try:
            with open(players, 'a') as file:
                file.write(fullname +", "+ email +", "+ phone +", "+ skillLevel + '\n')
        except IOError as e:
            print(f"Error writing to file '{players}': {e}")
        return render_template('thankyou.html')
    else:
        return render_template('signup.html')
    
@app.route('/volunteer.html', methods=['GET', 'POST'])
def volunteer():
    if request.method == 'POST':
        fullname = request.form.get('fullName')
        email = request.form.get('email')
        phone = request.form.get('phone')
        try:
            with open(volunteers, 'a') as file:
                file.write(fullname +", "+ email +", "+ phone + '\n')
        except IOError as e:
            print(f"Error writing to file '{volunteers}': {e}")
        return render_template('thankyouvolunteer.html')
    else:
        return render_template('volunteer.html')
    