from flask import Flask, request, render_template, redirect, url_for ,session
from flask_session import Session

app = Flask(__name__, static_url_path='/static')

app.config['SESSION_TYPE'] = 'filesystem'  # Loại session lưu trữ trên filesystem
app.config['SESSION_PERMANENT'] = False  # Sử dụng session phiên làm việc
app.config['SESSION_USE_SIGNER'] = True  # Sử dụng signer để bảo vệ session
app.secret_key = 'your_secret_key'  # Đặt secret key cho ứng dụng Flask
Session(app)
# Kết nối đến cơ sở dữ liệu SQL Server
import pyodbc

server = 'DESKTOP-MF3TM3N'
database = 'VGA_M_Hackathon'
username = 'nta1310'
password = '12345678'

connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server +
                           ';DATABASE=' + database +
                           ';UID=' + username +
                           ';PWD=' + password)

@app.route('/')
def login_form():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']

    print(email)
    password = request.form['password']
    print(password)
    # Thực hiện kiểm tra thông tin đăng nhập trong cơ sở dữ liệu
    cursor = connection.cursor()
    cursor.execute("select userID from [User] where gmail=? and password=?", (email, password))
    user = cursor.fetchone()

    if user:
        # Đăng nhập thành công
        # print("Đăng nhập thành công!")
        session['email'] = email
        return render_template('homepage.html')
    else:
        # Đăng nhập không thành công
        # print("Đăng nhập không thành công!")
        return "Đăng nhập không thành công!"
    
@app.route('/profile1')
def profile():
   
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True)
