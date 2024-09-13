from flask import Flask, render_template

application = Flask(__name__)
application.config.from_pyfile('config.cfg')

@application.route('/')
def index():
   return render_template('index.html',
      var=application.config['MY_VAR'])

if __name__ == '__main__':
   application.run()
