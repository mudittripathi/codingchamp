import flask
from flask import Flask       #flask module se Flask class import karayi
app = Flask(__name__)         #app define kia

@app.route("/")               # app me / lgadao, ek endpoint bnao..jo user yaha jao to run kr jaye mera progrm
def Hello():
    return 'Hello World'

@app.route("/harry")               # app me / lgadao, ek endpoint bnao..jo user yaha jao to run kr jaye mera progrm
def Harry():
    return 'Hello Harry'


app.run()                     #will give a localhost and it will display the result there.

# app.run(debug=True)     kch change agar apne kia to change detect krke reload krdega