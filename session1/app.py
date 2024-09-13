from flask import Flask, render_template, session, \
   request, redirect, url_for
from models import User

application = Flask(__name__)
application.config['SECRET_KEY'] = '1234567890987654321'

@application.route('/')
def index():
   if 'username' in session:
      username = session['username']
      return render_template('index.html', username=username)
   return redirect(url_for('login'))

@application.route('/login', methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
      username = request.form['username']
      password = request.form['password']
      user = User(username, password)
      if user.authenticate():
         session['username'] = username
         return redirect(url_for('index'))
      msg = 'Username/password salah.'
      return render_template('form.html', msg=msg)
   return render_template('form.html')

@application.route('/logout')
def logout():
   session.pop('username', None)
   return redirect(url_for('index'))

if __name__ == '__main__':
   application.run(debug=True)
