from flask import Flask, render_template, \
  request, redirect, url_for
import sqlite3, os

application = Flask(__name__)
application.config['DB_NAME'] = \
  os.getcwd() + '/flask-sqlite/database.db'

conn = cursor = None

def openDb():
   global conn, cursor
   conn = sqlite3.connect(application.config['DB_NAME'])
   cursor = conn.cursor()	

def closeDb():
   global conn, cursor
   cursor.close()
   conn.close()

@application.route('/')
def index():   
   openDb()
   container = []
   for id,judul,penulis,penerbit in \
   cursor.execute('SELECT * FROM buku'):	
		container.append((id,judul,penulis,penerbit))
   closeDb()
   return render_template('index.html', container=container)

@application.route('/tambah', methods=['GET','POST'])
def tambah():
   if request.method == 'POST':
      id = request.form['id']
      judul = request.form['judul']
      penulis = request.form['penulis']
      penerbit = request.form['penerbit']
      data = id, judul, penulis, penerbit
      openDb()
      cursor.execute('INSERT INTO buku VALUES(?,?,?,?)', data)
      conn.commit()
      closeDb()
      return redirect(url_for('index'))
   else:
      return render_template('tambah_form.html')

@application.route('/ubah/<id>', methods=['GET','POST'])
def ubah(id):
   openDb()
   result = cursor.execute('SELECT * FROM buku WHERE id=?', (id,))
   data = cursor.fetchone()
   if request.method == 'POST':
      id = request.form['id']
      judul = request.form['judul']
      penulis = request.form['penulis']
      penerbit = request.form['penerbit']
      cursor.execute('''
         UPDATE buku SET judul=?, penulis=?, penerbit=? 
         WHERE id=?
      ''', (judul, penulis, penerbit, id))
      conn.commit()
      closeDb()
      return redirect(url_for('index'))
   else:
      closeDb()
      return render_template('ubah_form.html', data=data)

@application.route('/hapus/<id>', methods=['GET','POST'])
def hapus(id):
   openDb()
   cursor.execute('DELETE FROM buku WHERE id=?', (id,))
   conn.commit()
   closeDb()
   return redirect(url_for('index'))

if __name__ == '__main__':
   application.run(debug=True)
