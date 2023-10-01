# from flask import Flask, request, render_template, redirect, url_for
from login import *  
# app = Flask(__name__, static_url_path='/static')

@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True)
