from flask import Flask, render_template, session

application = Flask(__name__)
application.config['SECRET_KEY'] = '1234567890987654321'

@application.route('/')
def index():
   msg = 'Session "var" telah dibuat.'
   session['var'] = 100
   return render_template('index.html', msg=msg)

@application.route('/ubahsession')
def ubahsession():
   session['var'] = 200
   msg = 'Nilai session "var" telah diubah.'
   return render_template('index.html', msg=msg)

@application.route('/hapussession')
def hapuscookie():
   if 'var' in session.keys():
      msg = 'Session "var" telah dihapus.'
      session.pop('var', None)
   else:
      msg = 'Session "var" tidak ditemukan'
   return render_template('index.html', msg=msg)

@application.route('/halaman1')
def halaman1():
   if 'var' in session.keys():
      var = session['var']
   else:
      var = None
   return render_template('halaman1.html', var=var)

@application.route('/halaman2')
def halaman2():
   if 'var' in session.keys():
      var = session['var']
   else:
      var = None
   return render_template('halaman2.html', var=var)

if __name__ == '__main__':
   application.run(debug=True)
