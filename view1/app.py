from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def index():
   response = render_template('header.html')
   response += render_template('content.html')
   response += render_template('footer.html')
   return response

if __name__ == '__main__':
   application.run(debug=True)
