from flask import Flask, render_template, request, redirect
from models import Produk

application = Flask(__name__)

@application.route('/')
def index():
   import sqlite3, os
   databaseName = os.getcwd() + '/model4/database.db'
   conn = sqlite3.connect(databaseName)
   cursor = conn.cursor()
   container = []
   for kode,nama,harga in cursor.execute('SELECT * FROM produk'):
		model = Produk(kode,nama,harga)
		container.append(model)
   cursor.close()
   conn.close()
   return render_template('index.html', container=container)

@application.route('/tambah', methods=['GET','POST'])
def tambah():
   if request.method == 'POST':
      kode = int(request.form['kode'])
      nama = request.form['nama']
      harga = float(request.form['harga'])
      model = Produk(kode,nama,harga)
      model.tambah()
      return redirect('http://localhost:5000')
   else:
      return render_template('tambah_form.html')

@application.route('/ubah/<int:id>', methods=['GET','POST'])
def ubah(id):
   model = Produk()
   model.load(id)
   if request.method == 'POST':
      kode = int(request.form['kode'])
      nama = request.form['nama']
      harga = float(request.form['harga'])
      model.setKode(kode)
      model.setNama(nama)
      model.setHarga(harga)
      model.ubah()
      return redirect('http://localhost:5000')
   else:
      return render_template('ubah_form.html', model=model)

@application.route('/hapus/<int:id>')
def hapus(id):
   model = Produk()
   model.load(id)
   model.hapus()
   return redirect('http://localhost:5000')

if __name__ == '__main__':
   application.run(debug=True)
