from flask import Flask, render_template

# mengimpor kelas Configuration 
# yang terdapat di dalam file config.py
from config import Configuration

application = Flask(__name__)
application.config.from_object(Configuration)

@application.route('/')
def index():
   return render_template('index.html',
      var=application.config['MY_VAR'])

if __name__ == '__main__':
   application.run()
