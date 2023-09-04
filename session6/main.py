from flask import Flask, request, jsonify, make_response, request, render_template, session, flash
import os
import jwt
from datetime import datetime, timedelta
from functools import wraps
import pytz


app = Flask(__name__)


app.config['SECRET_KEY'] = '<TOKEN>'


def token_required(func):
    # decorator factory which invoks update_wrapper() method and passes decorated function as an argument
    @wraps(func)
    def decorated(*args, **kwargs):
        headers = request.headers
        bearer = headers.get('Authorization')    # Bearer YourTokenHere
        token = bearer.split()[1]  # YourTokenHere
        if not token:
            return jsonify({'Alert!': 'Token is missing!'}), 401
        try:
            payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            print(payload)
        except:
            return jsonify({'Message': 'Invalid token'}), 403
        return func(*args, **kwargs)
    return decorated


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return 'logged in currently'

#Public page
@app.route('/public')
def public():
    return 'For Public'

#Private page
@app.route('/auth')
@token_required
def auth():
    return 'JWT is verified. Welcome to your dashboard !  '


@app.route('/login', methods=['POST'])
def login():
    if request.form['username'] and request.form['password'] == '123456':
        utc_bogota = datetime.now(pytz.timezone('America/Bogota'))
        session['logged_in'] = True
        # Standard UTC timezone aware Datetime
        aware = datetime.now(pytz.utc)
        print('Timezone Aware:',utc_bogota)
               
        token = jwt.encode({
            'user': request.form['username'],
            'expiration': str(utc_bogota + timedelta(seconds=30))
        },
            app.config['SECRET_KEY'],
            algorithm="HS256")
        return jsonify({'token': token})
    else:
        return make_response('Unable to verify', 403, {'WWW-Authenticate': 'Basic realm: "Authentication Failed "'})


@app.route('/logout', methods=['POST'])
def logout():
    pass
# your code goes here

    
"""
MAIN ...........................................................................
"""
if __name__ == '__main__':
    #app.run()
    app.run(debug=True, port=os.getenv("PORT", default=5000 )) 