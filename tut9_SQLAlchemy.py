# we will use sqlAlchemy - it is ORM

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
#
# ye sb import krna hai or ye command use krni hai app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
#
# database se connect krna
# search google sql data base sqlalchemy for mysql
#
# mysql://username:password@localhost/db_name
# db = SQLAlchemy(app)  -- ye initialization hai db initilaise krne ke lie
# uske bad class banana hai ab ye class humare database ke table ko define kregi

# contact form bharne ka tareeka
# post request marega ek page k wo wo page sarei values ko submit krega
# method = ["get", 'post']
# get method - koi image file fetch kr rhe hai to get se hoti hai
# koi index wo get request hoti hai
#
# post request secure rhti hai.. url me parameters ni ate
#
# iska sara kaam main.py me kia hua hai