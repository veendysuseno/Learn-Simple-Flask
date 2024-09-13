from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def index():
   a = 1
   b = 3
   return render_template('index.html', a=a, b=b)

if __name__ == '__main__':
   application.run(debug=True)
