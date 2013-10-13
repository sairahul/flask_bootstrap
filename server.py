
from flask import Flask, render_template
#from flask.ext.basicauth import BasicAuth

app = Flask(__name__)

# Example of basic authentication
"""
app.config['BASIC_AUTH_USERNAME'] = 'hello'
app.config['BASIC_AUTH_PASSWORD'] = 'helloworld'

basic_auth = BasicAuth(app)

@app.route('/upload')
@basic_auth.required
def secret():
    return render_template('secret.html')
"""

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
