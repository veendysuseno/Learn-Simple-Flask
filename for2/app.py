from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def index():
   import sqlite3
   conn = sqlite3.connect(':memory:')
   cursor = conn.cursor()
   cursor.execute('''
      CREATE TABLE produk (
         id INTEGER NOT NULL PRIMARY KEY,
         nama VARCHAR(25),
         harga FLOAT
      )
   ''')
   cursor.execute("INSERT INTO produk VALUES(?,?,?)",
      (1, 'Pensil', 6000))
   cursor.execute("INSERT INTO produk VALUES(?,?,?)",
      (2, 'Spidol', 8000))
   cursor.execute("INSERT INTO produk VALUES(?,?,?)",
      (3, 'Penggaris', 5000))
   conn.commit()
   result = cursor.execute("SELECT * FROM produk")
   data = []
   for kode, nama, harga in result:
		data.append((kode, nama, harga))
   cursor.close()
   conn.close()
   return render_template('index.html', data=data)

if __name__ == '__main__':
   application.run(debug=True)
