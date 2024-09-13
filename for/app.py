from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def index():
   dictionary = {
      '/': 'Home',
      '/produk': 'Produk dan Layanan',
      '/testimoni': 'Testimoni',
      '/kontak': 'Kontak'
   }
   return render_template('index.html', dictionary=dictionary)

@application.route('/produk')
def produk():
   return '<h2>Produk dan Layanan</h2>'

@application.route('/testimoni')
def testimoni():
   return '<h2>Testimoni</h2>'

@application.route('/kontak')
def kontak():
   return '<h2>Kontak</h2>'

if __name__ == '__main__':
   application.run(debug=True)
