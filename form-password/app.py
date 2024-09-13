from flask import Flask, render_template, request

application = Flask(__name__)

@application.route('/', methods=['GET', 'POST'])
def index():
   if request.method == 'POST':
      namaUser = request.form['namaUser']
      kataSandi = request.form['kataSandi']
      if namaUser=='python' and kataSandi=='Flask0.11':
         return render_template('response.html', 
            namaUser=namaUser)
      else:
         pesan = 'Anda tidak berhak menggunakan aplikasi ini.'
         return render_template('form.html', pesan=pesan)
   return render_template('form.html')

if __name__ == '__main__':
   application.run(debug=True)
