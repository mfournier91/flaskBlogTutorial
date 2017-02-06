from flask import render_template
from app import app

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

if __name__ == "__main__":
    app.run()