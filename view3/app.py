from flask import Flask, render_template, redirect

application = Flask(__name__)

@application.route('/')
def index():   
   return render_template('index.html')

@application.route('/python')
def python():
   return redirect('http://www.python.org')

@application.route('/ruby')
def ruby():
   return redirect('http://www.ruby-lang.org')

if __name__ == '__main__':
   application.run(debug=True)
