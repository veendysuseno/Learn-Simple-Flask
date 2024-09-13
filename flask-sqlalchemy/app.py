from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = \
   'sqlite:////' + os.path.join(basedir, 'database.db')
application.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# membuat objek dari kelas SQLAlchemy
db = SQLAlchemy(application)

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
