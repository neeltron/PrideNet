from flask import Flask, render_template, request



# Create a flask app
app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

def push_signup():





def verify_login():




def push_meet():




def push_forum():




@app.route('/')
def hello():
  return render_template('index.html')



@app.route('/VolunteerSignUp')
def signup():
  username_up = request.args.get('username')
  email = request.args.get('email')
  password_up = request.args.get('pass')
  dob = request.args.get('dob')
  return "Signed up successfully!"



@app.route('/VolunteerLogIn')
def login():
  username_in = request.args.get('username')
  password = request.args.get('pass')
  return "Logged in successfully!"



@app.route('/AnonymousLogIn')
def AnonymousLogIn():
  username = request.args.get('username')
  return "Logged in successfully!"



@app.route('/CreateMeetingRoom')
def CreateMeetingRoom():
  roomname = request.args.get('roomname')
  roomdesc = request.args.get('desc')
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
