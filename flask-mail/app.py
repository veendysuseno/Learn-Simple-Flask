from flask import Flask, render_template, request
from flask_mail import Mail, Message

application = Flask(__name__)
application.config['MAIL_SERVER'] = 'smtp.gmail.com'
application.config['MAIL_PORT'] = 587
application.config['MAIL_USE_TLS'] = True
application.config['MAIL_USE_SSL'] = False

@application.route('/', methods=['GET','POST'])
def index():
   if request.method == 'POST':
      gmail_username = request.form['gmail_username']
      gmail_password = request.form['gmail_password']
      to = request.form['to']
      subject = request.form['subject']
      message = request.form['message']
      
      application.config['MAIL_USERNAME'] = gmail_username
      application.config['MAIL_PASSWORD'] = gmail_password
      
      msg = Message(subject, 
         sender=gmail_username, recipients=[to])
      msg.body = message
      
      try:
         mail = Mail(application)
         mail.connect()
         mail.send(msg)
         return render_template('kirim_sukses.html', to=to)
      except:
         return render_template('kirim_gagal.html')
   return render_template('form.html')

if __name__ == '__main__':
   application.run(debug=True)
