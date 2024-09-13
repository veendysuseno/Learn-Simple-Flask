from flask import Flask, render_template, request
from models import User

application = Flask(__name__)

@application.route('/login', methods=['GET','POST'])
def index():
   model = User()
   if request.method == 'POST':
      username = request.form['username']
      password = request.form['password']
      model.setUsername(username)
      model.setPassword(password)
      if model.authenticate():
         return render_template('login_sukses.html', model=model)
      else:
         return render_template('login_error.html')
   else:
      return render_template('login_form.html', model=model)

if __name__ == '__main__':
   application.run(debug=True)
