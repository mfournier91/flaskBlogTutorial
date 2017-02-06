from flask import Flask

app = Flask(__name__) #app variable gets the flask instance
from app import views #app package used to import views