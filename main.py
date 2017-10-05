from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def signup():
    return render_template('signup.html')

@app.route("/signup", methods = ["POST"])
def validate():
    password = request.form['password']
    verify = request.form['verify']
    username = request.form['username']
    email = request.form['email']

    verify_error = ''
    password_error = ''
    username_error = ''
    email_error = ''
    
    #verify errors#
    if password != verify:
        verify_error = "Passwords do not match"
    
    #username errors#
    if username == '':
        username_error = "Username error"
    if len(username) > 20:
        username_error = "Username error"
    else:
        if len(username) < 3:
            username_error = "Username error"
    if ' ' in username:
        username_error = "Username error"

    #pssword errors#
    if password == '':
        password_error = "Password error"
    if len(password) > 20:
        password_error = "Password error"
    else:
        if len(password) < 3:
            password_error = "Password error"
    if ' ' in password:
        password_error = "Password error"

    #email errors#
    if (email != '') and (('@' and '.') not in email):
        email_error = "Email not formatted properly"
    if email.count('@') >= 2:
        email_error = "Email not formatted properly"
    if email.count('.') >=2:
        email_error += "Email not formatted properly"

    if not verify_error and not password_error and not username_error and not email_error:
        return render_template('welcome.html', username = username)
    else:
        return render_template('signup.html', password_error=password_error, 
            username_error=username_error, 
            verify_error=verify_error,
            email_error=email_error,
            username = username,
            email = email)
app.run()