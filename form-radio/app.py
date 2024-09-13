from flask import Flask, render_template, request

application = Flask(__name__)

@application.route('/', methods=['GET', 'POST'])
def index():
   if request.method == 'POST':
      nama = request.form['nama']
      gender = request.form['gender']
      agama = int(request.form['agama'])      
      return render_template('response.html', 
         nama=nama, gender=gender, agama=agama)
   return render_template('form.html')

if __name__ == '__main__':
   application.run(debug=True)
