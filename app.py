from flask import Flask, render_template, request, redirect, url_for
import hashlib  # for password hashing

app = Flask(__name__)

users = {
    "user": "88162595c58939c4ae0b35f39892e6e7"  # 'new_password' hashed with MD5
}


@app.route('/')
def login_page():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users:
        # Verify the password
        if hashlib.md5(password.encode()).hexdigest() == users[username]:
            return "Login Successfully . WELCOME."
        else:
            return "Incorrect password. Please try again."
    else:
        return "Username not found. Please register."


if __name__ == '__main__':
    app.run(debug=True)
