from flask import Flask, render_template, request

# Create a flask app
app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

# Index page
@app.route('/')
def hello():
  return render_template('index.html')



@app.route('/VolunteerSignUp')
def signup():
  username = request.args.get('username')
  email = request.args.get('email')
  password = request.args.get('pass')
  dob = request.args.get('dob')
  return "Signed up successfully!"



@app.route('/VolunteerLogIn')
def login():
  return "Logged in successfully!"



@app.route('/AnonymousLogIn')
def AnonymousLogIn():
  return "Logged in successfully!"



@app.route('/CreateMeetingRoom')
def CreateMeetingRoom():
  return "Successfully created a meeting room!"



@app.route('/PostInForum')
def PostInForum():
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
