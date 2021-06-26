from flask import Flask, render_template, request
import mysql.connector
import os



# Create a flask app
app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

hostname = os.environ['host']
user = os.environ['user']
dbname = os.environ['dbname']
dbpass = os.environ['dbpass']
db = mysql.connector.connect(host = hostname, user = user, password = dbpass, database = dbname)
cursor = db.cursor()

def push_signup(username_up, email, password_up, dob):
  sql = "INSERT INTO accounts (username, email, password, dob) values ('" + username_up + "', '" + email + "', '" + password_up + "', '" + dob + "')"
  cursor.execute(sql)
  db.commit()



def verify_login(username_in, pass_in):
  sql = "SELECT * FROM accounts WHERE username = '" + username_in + "' AND password = '" + pass_in +"'"
  cursor.execute(sql)
  res = cursor.fetchall()
  count = 0
  for epoch in res:
    count += 1
  
  if count == 0:
    return "Invalid Username/Password"
  else:
    return "Success"



def push_meet(name, desc):
  sql = "INSERT INTO meet (name, description) values ('" + name + "', '" + desc + "')"
  cursor.execute(sql)
  db.commit()



# def push_forum():




@app.route('/')
def hello():
  return render_template('index.html')



@app.route('/VolunteerSignUp')
def signup():
  username_up = request.args.get('username')
  email = request.args.get('email')
  password_up = request.args.get('pass')
  dob = request.args.get('dob')
  push_signup(username_up, email, password_up, dob)
  return "Signed up successfully!"



@app.route('/VolunteerLogIn')
def login():
  username_in = request.args.get('username')
  password = request.args.get('pass')
  response = verify_login(username_in, password)
  return response



@app.route('/CreateMeetingRoom')
def CreateMeetingRoom():
  roomname = request.args.get('roomname')
  roomdesc = request.args.get('desc')
  push_meet(roomname, roomdesc)
  return "Successfully created a meeting room!"



@app.route('/PostInForum')
def PostInForum():
  roomname = request.args.get('username')
  roomdesc = request.args.get('post')
  return "Posted successfully!"



@app.route('/ViewForum')
def ViewForum():
  return "Here are the posts:"



if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )
