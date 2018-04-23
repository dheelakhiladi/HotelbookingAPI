from flask import Flask 
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from flask_mysqldb import MySQL
import os
app= Flask(__name__)



mysql = MySQL(app)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sonyvaio'
app.config['MYSQL_DB'] = 'hotel'


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('Booking details.html')

@app.route('/login',methods = ['POST'])
def do_admin_login():
    if request.form['password'] == '12345' and request.form['username'] == 'admin':
        session ['logged_in'] = True
    else:
        flash('Wrong Password !')
    return home()
@app.route("/logout")
def logout():
    session[logged_in] = False
    return home()
@app.route('/CheckAvailability', methods = ['POST'])
def CheckAvailability():
    cursor = mysql.connection.cursor()
    currCheckinDate=request.form['CheckinDate']
    currCheckoutDate=request.form['CheckoutDate']
    session['currCheckinDate'] = currCheckinDate
    session['currCheckoutDate'] = currCheckoutDate
    if currCheckoutDate<=currCheckinDate:
        flash("Invalid dates")
        return render_template('Booking details.html')
        pass
    else:
        query = "select id from visitors where id not in(select id from visitors where ("+currCheckinDate+">CheckoutDate) or ("+currCheckoutDate+"<CheckinDate) )"
        query2 = "select id , RoomType from room where id not in("+query+")"
        cursor.execute(query2)
        if cursor.rowcount !=0:
            data = cursor.fetchall()
            return render_template('Room_Book.html', data=data)
        else:
            return "No Rooms Available"

@app.route('/book', methods = ['POST'])
def book():
    room = request.form['rno']
    print room
    session['room'] = room
    return render_template('/GetDetails.html',)
    
@app.route('/Dbwrite', methods=['POST'])
def write():
    cursor = mysql.connection.cursor()
    room = session.get('room')
    currCheckinDate = session.get('currCheckinDate')
    currCheckoutDate = session.get('currCheckoutDate')
    rnos = room.split(",")
    name = request.form['Name']
    gender = request.form['gender']
    phone = request.form['Phone']
    ID = request.form['idproof']

    for i in rnos:
        W_query = "insert into visitors (Name,PhoneNo,VisitorsId,CheckinDate,CheckoutDate,RoomNo,Gender) values('"+str(name)+" ', '"+str(phone)+"' , '"+str(ID)+"', '" +str(currCheckinDate)+"', ' "+str(currCheckoutDate)+"', ' "+str(i)+"','"+str(gender[0])+"');"
        cursor.execute(W_query)
        mysql.connection.commit()
    return "Booking Successfull"
if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(debug=True, host = '0.0.0.0', port = 4001)
    pass

  

