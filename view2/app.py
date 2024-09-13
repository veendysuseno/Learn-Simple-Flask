from flask import Flask, redirect

application = Flask(__name__)

@application.route('/')
def index():   
   return redirect('/welcome')

@application.route('/welcome')
def welcome():
   response = '''
      <h2>Demo Fungsi View 2</h2>
      <p>Contoh penggunaan fungsi redirect()</p>
   '''
   return response

if __name__ == '__main__':
   application.run(debug=True)
