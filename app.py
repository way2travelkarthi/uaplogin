
import pyrebase
from flask import Flask,render_template, request

app = Flask(__name__) 

#Add your own details
config = {
  "apiKey": "AIzaSyCpueysTCJjIjW8t3-r-gV4NOPrZY2VZbA",
  "authDomain": "university-admit-predictor.firebaseapp.com",
  "databaseURL": "https://university-admit-predictor-default-rtdb.firebaseio.com",
  "projectId": "university-admit-predictor",
  "storageBucket": "university-admit-predictor.appspot.com",
  "messagingSenderId": "471033088541",
  "appId": "1:471033088541:web:2d05bfca07ad298f2cd4f4",
  "measurementId": "G-DCEHDHRG4K"
}

#initialize firebase
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

@app.route('/register', methods = ["POST", "GET"])
def regiter():
    if request.method == "POST":
        name=request.form.get('name')
        email=request.form.get('email')
        password=request.form.get('pass')
        cpassword=request.form.get('cpass')
    try:
        if(password==cpassword):
            user=auth.create_user_with_email_and_password(email,password)
            return render_template("login.html")
    except:
        return render_template("signup.html",cerror="Your passwaord could not be same or Already Exist account")
#Login
@app.route('/')
def login():
    return render_template("login.html")

#Sign up/ Register
@app.route('/signup')
def signup():
    return render_template("signup.html")

#Welcome page
@app.route('/welcome')
def welcome():
   return render_template("welcome.html",name=name)

@app.route('/logout',methods=["POST","GET"])
def logout():
    return render_template("login.html")  
#If someone clicks on login, they are redirected to /result
@app.route('/result', methods = ["POST", "GET"])
def result():
    if request.method == "POST":        
        email=request.form.get('email')
        password=request.form.get('pass')
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            return render_template("welcome.html")
        except:
            return render_template("login.html",error="Your Email and Password Invalid Please Try login again or SignUp")
if __name__ == "__main__":
    app.run(debug=True)
