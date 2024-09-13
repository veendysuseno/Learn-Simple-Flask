from flask import Flask, render_template, \
  request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = \
   'sqlite:////' + os.path.join(basedir, 'database.db')
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# membuat objek dari kelas SQLAlchemy
db = SQLAlchemy(application)

# mendefinisikan model
class Buku(db.Model):
   __tablename__ = 'buku'
   id = db.Column(db.String(4), primary_key=True)
   judul = db.Column(db.String(40), unique=True)
   penulis = db.Column(db.String(25))
   penerbit = db.Column(db.String(30))

   def __init__(self, id, judul, penulis, penerbit):
      self.id = id
      self.judul = judul
      self.penulis = penulis
      self.penerbit = penerbit

   def __repr__(self):
      return '[%s, %s, %s, %s]' % \
         (self.id, self.judul, self.penulis, self.penerbit)

@application.route('/')
def index():   
   return render_template('index.html', container=Buku.query.all())

@application.route('/tambah', methods=['GET','POST'])
def tambah():
   if request.method == 'POST':
      id = request.form['id']
      judul = request.form['judul']
      penulis = request.form['penulis']
      penerbit = request.form['penerbit']
      buku = Buku(id, judul, penulis, penerbit)
      db.session.add(buku)
      db.session.commit()
      return redirect(url_for('index'))
   else:
      return render_template('tambah_form.html')

@application.route('/ubah/<id>', methods=['GET','POST'])
def ubah(id):   
   buku = Buku.query.filter_by(id=id).first()
   if request.method == 'POST':           
      buku.id = request.form['id']
      buku.judul = request.form['judul']
      buku.penulis = request.form['penulis']
      buku.penerbit = request.form['penerbit']
      db.session.add(buku)
      db.session.commit()
      return redirect(url_for('index'))
   else:      
      return render_template('ubah_form.html', buku=buku)

@application.route('/hapus/<id>', methods=['GET','POST'])
def hapus(id):
   buku = Buku.query.filter_by(id=id).first()
   db.session.delete(buku)
   db.session.commit()
   return redirect(url_for('index'))

if __name__ == '__main__':
   application.run(debug=True)
