from flask import Flask, render_template, request

application = Flask(__name__)

@application.route('/', methods=['GET', 'POST'])
def index():
   if request.method == 'POST':
      agama = int(request.form['agama'])
      bahasa = request.form.getlist('bahasa')
      return render_template('response.html', 
         agama=agama, bahasa=bahasa)
   return render_template('form.html')

if __name__ == '__main__':
   application.run(debug=True)
