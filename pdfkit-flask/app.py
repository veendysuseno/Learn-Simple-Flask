from flask import Flask, render_template
import pdfkit
import os

application = Flask(__name__)
application.config['PDF_FOLDER'] = os.path.realpath('.') + \
   '/pdfkit-flask/static/pdf'
application.config['TEMPLATE_FOLDER'] = os.path.realpath('.') + \
   '/pdfkit-flask/templates'

@application.route('/')
def index():
   return render_template('index.html')

@application.route('/konversi')
def konversi():
   htmlfile = application.config['TEMPLATE_FOLDER'] + '/index.html'
   pdffile = application.config['PDF_FOLDER'] + '/demo4.pdf'
   pdfkit.from_file(htmlfile, pdffile)
   return '''
     Proses konversi ke PDF telah berhasil dilakukan.<br />Klik
     <a href="http://localhost:5000/static/pdf/demo4.pdf">di sini</a> 
     untuk membuka file tersebut.
   '''

if __name__ == '__main__':
   application.run(debug=True)
