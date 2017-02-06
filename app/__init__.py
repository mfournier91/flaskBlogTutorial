from flask import Flask

app = Flask(__name__) #app variable gets the flask instance
app.config.from_object('config')

from app import views #app package used to import views