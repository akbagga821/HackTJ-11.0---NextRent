from flask import Flask, render_template, request
import sqlite3
import requests # third party - not flask
import json


app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('homescapes_database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def start_form():
    return render_template('start.html')


@app.route('/blank')
def temproute():
    return render_template('temp.html')


@app.route('/intermediate', methods=['POST'])
def intermediate():
    if request.method == 'POST':
        email = request.form.get('f_email')
        namee = request.form.get('f_name')
        password = request.form.get('f_password')
    print(email, namee, password)
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (c_email, c_name, c_pass, c_home1, c_home2, c_home3) VALUES (?, ?, ?, ?, ?, ?)", (email, namee, password, " ", " ", " "))
    conn.commit()
    cur.close()
    return render_template('home_page0.html', name=namee)


@app.route('/middleware')
def middle():
    return render_template('questionaire.html')
    

def update_homes(name, ownerName):
    print(name, ownerName)
    conn = get_db_connection()
    cur = conn.cursor()
    data1 = conn.execute("SELECT c_home1 FROM users WHERE c_email = ?", (ownerName,)).fetchall()
    data2 = conn.execute("SELECT c_home2 FROM users WHERE c_email = ?", (ownerName,)).fetchall()
    data3 = conn.execute("SELECT c_home3 FROM users WHERE c_email = ?", (ownerName,)).fetchall()
    print('djflskj;fds')
    home1 = data1[0][0]
    home2 = data2[0][0]
    home3 = data3[0][0]
    print(home1, home2, home3)
    if home1 == " ":
        cur.execute('UPDATE users SET c_home1=? WHERE c_email = ?',(name,ownerName,))
    elif home2 == " ":
        cur.execute('UPDATE users SET c_home2=? WHERE c_email = ?',(name,ownerName,))
    elif home3 == " ":
        cur.execute('UPDATE users SET c_home3=? WHERE c_email = ?',(name,ownerName,))
    conn.commit()
    cur.close()



@app.route('/homescape', methods=["POST", "GET"])
def homescape():
    if request.method == 'POST':
        rooms1 = request.form.get('roomieForm')
        num = request.form.get('roomieNums')
        h_name = request.form.get('homescapeName')
        u_name = request.form.get('ownerName')
        #rooms2 = request.form.get('Altroomie')
        update_homes(h_name, u_name)
        num = int(num)
        print(rooms1)
        print(num)
        for i in range(num):
            id = "Altroomie" + str(i)
            print(id)
            rooms2 = request.form.get(id)
            print(rooms2)
    return render_template('homescape.html', hname='Melon', t='Electric Bill', freq='1', c='167')


@app.route('/expenses')
def expenses():
    return render_template('expense.html')


@app.route('/expensed', methods=['POST'])
def expensed():
    homescape_name = request.form.get('category')
    title = request.form.get('namee')
    frequency = request.form.get('freqs')
    cost = request.form.get('costy')
    return render_template('homescape.html', hname=homescape_name, t=title, freq=frequency, c=cost)


@app.route('/home', methods=['POST', 'GET'])
def process():
    if request.method == 'POST':
        email = request.form.get('f_email')
        password = request.form.get('f_password')
        print(email, password)
        conn = get_db_connection()
        data = conn.execute("SELECT c_name FROM users WHERE c_email = ?", (email,)).fetchall()
        data1 = conn.execute("SELECT c_home1 FROM users WHERE c_email = ?", (email,)).fetchall()
        data2 = conn.execute("SELECT c_home2 FROM users WHERE c_email = ?", (email,)).fetchall()
        data3 = conn.execute("SELECT c_home3 FROM users WHERE c_email = ?", (email,)).fetchall()
        home1 = data1[0][0]
        home2 = data2[0][0]
        home3 = data3[0][0]
        print(home1, home2, home3)
        if home3 != " ":
            print('3dddd')
            return render_template('home_page3.html', name=data[0][0], h1=home1, h2=home2, h3=home3)
        elif home2 != " ":
            print('2eddddd')
            return render_template('home_page2.html', name=data[0][0], h1=home1, h2=home2)
        elif home1 != " ":
            print('1ddddfd')
            return render_template('home_page1.html', name=data[0][0], h1=home1)
        return render_template('home_page0.html', name=data[0][0])
    return render_template('home_page1.html', name='Akansha Bagga', h1='Melon')
'''
@app.route('/homescape1')
def homescape1():
    return render_template('expense.html')'''
    
app.debug = True
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)