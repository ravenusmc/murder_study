#importing outside libraries for use in the project
from flask import Flask, session, jsonify, redirect, url_for, escape, render_template, request, flash
import matplotlib.pyplot as plt, mpld3
import numpy as np
import pandas as pd

#importing files that I made for the program
from client import *
from data import *

#Setting up Flask
app = Flask(__name__)

#This function brings the user to the login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #Recieving the information from the form from the user.
        username = request.form['username']
        password = request.form['password']
        #Creating the object that will represent the user.
        user = User(username)
        #Now checking to see if the user is in the database.
        flag = user.check(username, password)
        #Conditional statement to test if the user is a member of the site.
        if flag == True:
            #If the user is in the database, the user gets sent to the index page.
            session['username'] = request.form['username']
            #Sending the user to the index page
            return redirect(url_for('index'))
        else:
            #If the user is not in the database then they will be sent to the
            #sign up page.
            return redirect(url_for('sign_up'))
    return render_template('login.html', title='Login Page')

#This function brings the user to the sign up page
@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        #Getting the correct data from the form that was submitted.
        username = request.form['username']
        password = request.form['password']
        password_check = request.form['second_password']
        #using a flash message to ensure that the first and second passwords match.
        if password != password_check:
            flash('The Passwords must match')
            return redirect(url_for('sign_up'))
        #Creating the object that will represent the user.
        user = User(username)
        #Encrypting the password
        password, hashed = user.encrypt_pass(password)
        #Adding the user to the database
        user.add(username, hashed)
        #Letting them into the index Page
        return redirect(url_for('index'))
    return render_template('sign_up.html', title='Sign Up Page')

#This function brings the user to the home page
@app.route('/index')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('index.html', title="Home Page")

#This function looks at the murders by year
@app.route('/_by_year')
def by_year():
    #Creating an object that will be used to analyze data by the year
    data = Data()
    #pulling the data from what the user entered
    year = request.args.get('year', 0, type=int)
    year = data.by_year(year)
    return jsonify(result = year)

#This function looks at the murders by state
@app.route('/_by_state')
def by_state():
    #Creating an object that will be used to analyze data by the year
    data = Data()
    #pulling the data from what the user entered
    state = request.args.get('state', 0, type=str)
    #Capitalizing the state name to ensure that it matches what is in the csv file
    state = state.title()
    #Returning the murder count in the state by using the by_state method in the
    #data.py file.
    state_count = data.by_state(state)
    #Returning the state count back to the user.
    return jsonify(result = state_count)

#This function looks at the murders by both state and year
@app.route('/_by_state_year')
def by_state_year():
    #Creating an object that will be used to analyze data by the year
    data = Data()
    #These next two lines pull the data from what the user entered
    state = request.args.get('state_name', 0, type=str)
    year = request.args.get('year_two', 0, type=int)
    #Using the .title method to ensure that states with two words appear the
    #same as they are in the csv
    state = state.title()
    #Calling the by_state_year method in the data.py file to get the number of
    #murders for the data that was entered.
    state_year_count = data.by_state_year(state, year)
    #Returning the state count back to the user.
    return jsonify(result = state_year_count)

#This function looks at the sex's of the victims and the Perpetrator.
@app.route('/_by_sex')
def by_sex():
    #Creating an object that will be used to analyze data by the year
    data = Data()
    #Creating a list to hold my three variables in.
    data_list = []
    #Getting the data that the user entered
    sex_one = request.args.get('sex_one', 0, type=str)
    sex_two = request.args.get('sex_two', 0, type=str)
    #I have to ensure that male and female are uppercase.
    sex_one = sex_one.title()
    sex_two = sex_two.title()
    #Calling the by_sex method to find the data that I need
    count = data.by_sex(sex_one, sex_two)
    #Appending all three of my variables to the list-may be better way to do
    #this
    data_list.append(sex_one)
    data_list.append(sex_two)
    data_list.append(count)
    #Returning the result
    return jsonify(result = data_list)

#This function will take the user to the graph page
@app.route('/graphs')
def graphs():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('graph.html', title="Graph Page")

#This function is what will log out the user.
@app.route('/sign_out')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('login'))

# set the secret key. keep this really secret:
app.secret_key = 'n3A\xef(\xb0Cf^\xda\xf7\x97\xb1x\x8e\x94\xd5r\xe0\x11\x88\x1b\xb9'

#This line will actually run the app.
if __name__ == '__main__':
    app.run(debug=True)
