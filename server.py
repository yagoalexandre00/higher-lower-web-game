from flask import Flask
from random import randint

correct_number = randint(0, 9)
app = Flask(__name__)

def make_bold(function):
    def wrap():
        data = function()
        return f"<b>{data}</b>"
    return wrap

@app.route('/')
@make_bold
def guess_a_number():
    return "<h1>Hey, guess a number between 0 and 9!</h1>" \
           "<p>Write after the '5000/' URL</p>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"
           
@app.route('/<int:user_choice>')
def is_correct(user_choice):
    if user_choice > 9:
        return f"<h1>HEY, WHO ARE YOU TRYING TO CHEAT????? 🧐</h1>" \
                "<img src='https://media.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif'>"
    elif user_choice == correct_number:
        return f"<h1>Oh no. You found me 🤭</h1>" \
                "<img src='https://media.giphy.com/media/ICOgUNjpvO0PC/giphy.gif'>"
    elif user_choice < correct_number:
        return f"<h1>That's too low 😋</h1>" \
                "<img src='https://media.giphy.com/media/l4KibK3JwaVo0CjDO/giphy.gif'>"
    elif user_choice > correct_number:
        return f"<h1>Wow... That's too high 🤪</h1>" \
                "<img src='https://media.giphy.com/media/S6VGjvmFRu5Qk/giphy.gif'>"
    
if __name__ == "__main__":
    app.run()