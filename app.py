from flask import Flask, render_template, request, jsonify
import discord
import os
from threading import Thread
import asyncio


app = Flask(__name__)

DISCORD_BOT_TOKEN = os.environ.get('DISCORD_BOT_TOKEN')
SIGNUP_CHANNEL_ID = 1392243683046199366       
VOLUNTEER_CHANNEL_ID = 1392243711412277279 

intents = discord.Intents.default()
intents.message_content = True 
client = discord.Client(intents=intents)

bot_ready = False
@client.event
async def on_ready():
    global bot_ready
    bot_ready = True

def run_discord_bot():

    client.run(DISCORD_BOT_TOKEN)


discord_thread = Thread(target=run_discord_bot)
discord_thread.daemon = True # Allows the main program to exit even if this thread is still running
discord_thread.start()


@app.route('/')
def main():
    if bot_ready:
            print("tried to type")
            asyncio.run_coroutine_threadsafe(
                        send_discord_message(SIGNUP_CHANNEL_ID, "testing testing"), client.loop
                    )
    return render_template('main.html')


@app.route('/signup.html', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        fullname = request.form.get('fullName')
        email = request.form.get('email')
        phone = request.form.get('phone')
        skillLevel = request.form.get('skillLevel')
        message = (
            f"**New Signup Form Submission:**\n"
            f"**Full Name:** {fullname}\n"
            f"**Email:** {email}\n"
            f"**Phone:** {phone}\n"
            f"**Skill Level:** {skillLevel}"
        )
        if bot_ready:
            asyncio.run_coroutine_threadsafe(
                        send_discord_message(SIGNUP_CHANNEL_ID, message), client.loop
                    )
        
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
            f"**Phone:** {phone}"
        )
        if bot_ready:
            print("tried to type")
            asyncio.run_coroutine_threadsafe(
                        send_discord_message(VOLUNTEER_CHANNEL_ID, message), client.loop
                    )

        return render_template('thankyouvolunteer.html')
    else:
        return render_template('volunteer.html')
    

async def send_discord_message(channel_id, message_content):    
    channel = client.get_channel(channel_id)
    if channel:
            print("tried to type")
            await channel.send(message_content)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    

