from flask import Flask, render_template
from models import ArticleModel

application = Flask(__name__)

content = '''
Python adalah bahasa pemrograman yang saat ini mulai marak digunakan 
untuk mengembangkan program di segala bidang. Jenis program yang 
dapat dibuat juga beragam; bisa berupa command-line interface (CLI),
graphical user interface (GUI), maupun program berbasis web.
'''

@application.route('/')
def index():
   # membuat objek dari kelas ArticleModel
   model = ArticleModel()
   
   # mengisi nilai ke dalam model
   model.setTitle('Apa Itu Python?')
   model.setDate('01/10/2016')
   model.setContent(content)   
   
   # mengirim nilai ke view
   return render_template('article.html',
      judul=model.getTitle(),
      tanggal=model.getDate(),
      isi=model.getContent())

if __name__ == '__main__':
   application.run(debug=True)
