from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def index():
   a = 10
   b = 3
   
   # mengirim nilai a dan b ke template
   return render_template('index.html', a=a, b=b)

if __name__ == '__main__':
   application.run(debug=True)
