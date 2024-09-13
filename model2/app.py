from flask import Flask, render_template, request
from models import Lingkaran

application = Flask(__name__)

@application.route('/', methods=['GET','POST'])
def index():
   if request.method == 'POST':
      model = Lingkaran()
      model.setRadius(float(request.form['radius']))
      return render_template('lingkaran.html', model=model)
   else:
      return render_template('form.html')

if __name__ == '__main__':
   application.run(debug=True)
