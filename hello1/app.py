from flask import Flask

application = Flask(__name__)

@application.route('/')
def index():
   return '<h2>Hello World!</h2>'

@application.route('/hello/<name>')
def hello(name):
   return '<h2>Hello %s</h2>' % name

@application.route('/page/<int:number>')
def page(number):
   return '<h2>Page #%d</h2>' % number

if __name__ == '__main__':
   application.run(debug=True)
