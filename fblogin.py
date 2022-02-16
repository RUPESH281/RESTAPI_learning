from flask import Flask, redirect, url_for, session
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)

app.secret_key = "APP_SECRET_KEY"

oauth = OAuth(app)
facebook = oauth.register(
    name='facebook',
    client_id='519684322797530',
    client_secret='b8c5037e479cf1f79fb1b433d75569e2',
    access_token_url='https://graph.facebook.com/oauth/access_token',
    access_token_params=None,
    authorize_url='https://www.facebook.com/dialog/oauth',
    authorize_params=None,
    api_base_url='https://graph.facebook.com/',
    client_kwargs={'scope': 'email'},
)


@app.route('/')
def hello_world():
    email = dict(session).get('email', None)
    return f'Hello!'


@app.route('/login')
def login():
    facebook = oauth.create_client('facebook')
    redirect_uri = url_for('authorize', _external=True)
    return facebook.authorize_redirect(redirect_uri)


@app.route('/authorize')
def authorize():
    facebook = oauth.create_client('facebook') 
    token = facebook.authorize_access_token()
    resp = facebook.get('userinfo')
    user_info = resp.json()
    session['profile'] = user_info
    session.permanent = True
    return redirect('/')


@app.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)