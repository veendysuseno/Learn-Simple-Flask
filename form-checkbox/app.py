from flask import Flask, render_template, request

application = Flask(__name__)

@application.route('/', methods=['GET', 'POST'])
def index():
   if request.method == 'POST':
      frameworks = request.form.getlist('frameworks')
      return render_template('response.html', 
         frameworks=frameworks)
   return render_template('form.html')

if __name__ == '__main__':
   application.run(debug=True)
