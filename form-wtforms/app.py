from flask import Flask, render_template, request
from models import LoginForm

application = Flask(__name__)
application.config['SECRET_KEY'] = '@#$123456&*()'

@application.route('/', methods=['GET', 'POST'])
def index():
   form = LoginForm()
   if request.method == 'POST':
      namaUser = form.namaUser.data
      kataSandi = form.kataSandi.data
      if namaUser=='admin' and kataSandi=='flask':
         return render_template('response.html', namaUser=namaUser)
      else:
         pesan = 'Anda tidak berhak menggunakan aplikasi ini.'
         return render_template('form.html', form=form, pesan=pesan)
   return render_template('form.html', form=form)

if __name__ == '__main__':
   application.run(debug=True)
