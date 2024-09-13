from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def index():
   
   # terdapat dua karakter spasi di belakang teks
   var = 'Belajar <strong>Python</strong> dan <em>Flask</em>  '
   
   return render_template('index.html', var=var)

if __name__ == '__main__':
   application.run(debug=True)
