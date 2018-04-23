from flask import Flask 
from flask_mysqldb import MySQL 

app= Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sonyvaio'
app.config['MYSQL_DB'] = 'example'
mysql = MySQL(app)
@app.route('/')
def index():
	cur = mysql.connection.cursor()
	cur.execute(''' SELECT * FROM hello ''')
	rv = cur.fetchall()
	return str(rv)

if __name__ == '__main__':
	app.run(debug=True)
	pass

