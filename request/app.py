from flask import Flask, request

application = Flask(__name__)

@application.route('/')
def index():
   # mengambil header dari objek request
   headers = request.headers
   response = [ '%s = %s' % (key, value) \
      for key, value in sorted(headers.items())
   ]
   response = '<br/>'.join(response)
   return response

if __name__ == '__main__':
   application.run(debug=True)
