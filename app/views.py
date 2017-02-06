from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index() :
    user = {'nickname': 'Marc'}  # fake user
    posts = [
        {
            'author': {'nickname': 'Alice'},
            'body': 'Portlandia is my life'
        },
        {
            'author': {'nickname': 'Bob'},
            'body': 'Avengers was dope'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
                           title="Sign in",
                           form=form)

if __name__ == "__main__":
    app.run()