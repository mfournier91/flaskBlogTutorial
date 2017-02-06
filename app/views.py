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
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title="Sign in",
                           form=form)

if __name__ == "__main__":
    app.run()