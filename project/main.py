#importing outside libraries for use in the project
from flask import Flask, session, redirect, url_for, escape, render_template, request, flash

#importing files that I made for the program
from client import *

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

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    return render_template('sign_up.html', title='Sign Up Page')

# set the secret key. keep this really secret:
app.secret_key = 'n3A\xef(\xb0Cf^\xda\xf7\x97\xb1x\x8e\x94\xd5r\xe0\x11\x88\x1b\xb9'

#This line will actually run the app.
if __name__ == '__main__':
    app.run(debug=True)
