import mysql.connector
from mysql.connector import Error
from sqlalchemy import null

def connection():
	try:
		connection = mysql.connector.connect(host='localhost',
											database='food-estimation',
											user='root',
											password='')
		return connection
	except Error as e:
		print("Error while connecting to MySQL", e)
		return null
	
def login_data(user,password):
	connect=connection()
	if(connect):
		mycursor = connect.cursor()
		mycursor.execute("SELECT * FROM users where username like '"+user+"'")
		myresult = mycursor.fetchone()
		if(myresult):
			if(myresult[1]==password):
				msg=1
			else:
				msg=0
		else:
			msg= 0
		if connect.is_connected():
			mycursor.close()
			connect.close()
			print("MySQL connection is closed")
	else:
		msg= 0
	return msg
	
def registeration(user,password,cpass,email,gender,age,health_issues):
	connect=connection()
	if(connect):
		mycursor = connect.cursor()
		mycursor.execute("SELECT * FROM users where username like '"+user+"'")
		myresult = mycursor.fetchone()
		if(myresult):
			return "existed"
		else:
			if(password==cpass):
				try:
					
					sql = "INSERT INTO users(username, password, email, gender, age, health_issues) VALUES ('"+user+"','"+password+"','"+email+"','"+gender+"','"+age+"','"+health_issues+"')"
					mycursor.execute(sql)
					connect.commit()
					if connect.is_connected():
						mycursor.close()
						connect.close()
						print("MySQL connection is closed")
					return "success"
				except:
					return "error"

			else:
				return "password"
	else:
		return "error"

def get_data(user):
	connect=connection()
	if(connect):
		mycursor = connect.cursor()
		mycursor.execute("SELECT * FROM users where username like '"+user+"'")
		myresult = mycursor.fetchone()
		if(myresult):
			age=myresult[4]
			gender=myresult[3]
			health_issues=myresult[5]
			return (age,gender,health_issues)
		else:
			return "","",""
	else:
		return "","",""

