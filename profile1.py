from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return 'Welcome to the Home Page'

@app.route('/profile1')
def profile():
    return render_template('profile1.html')

if __name__ == '__main__':
    app.run(debug=True)
