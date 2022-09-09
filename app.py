
import pyrebase
from flask import Flask,render_template, request

app = Flask(__name__)       #Initialze flask constructor

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
#db = firebase.database()

@app.route("/register", methods = ["POST", "GET"])
def regiter():
    if request.method == "POST": 
        global name       #Only if data has been posted
        name=request.form.get('name')
        email=request.form.get('email')
        password=request.form.get('pass')
        cpassword=request.form.get('cpass')
    try:
        if(password==cpassword):
            user=auth.create_user_with_email_and_password(email,password)
            
            return render_template("login.html")
    #return render_template("login.html")
    except:
        #return "Your passwaord could not be same Please Try Again"
        return render_template("signup.html",cerror="Your passwaord could not be same or Already Exist account")

"""#Initialze person as dictionary
person = {"is_logged_in": False, "name": "", "email": "", "uid": ""}
"""
#Login
@app.route("/")
def login():
    return render_template("login.html")

#Sign up/ Register
@app.route("/signup")
def signup():
    return render_template("signup.html")

#Welcome page
@app.route("/welcome")
def welcome():
   # if session["is_logged_in"] == True:
   #name=auth.get_account_info('name')
   return render_template("welcome.html",name=name)
@app.route("/logout",methods=["POST","GET"])
def logout():
    auth.current_user = None
    return render_template("login.html")  
#If someone clicks on login, they are redirected to /result
@app.route("/result", methods = ["POST", "GET"])
def result():
    """if('user' in session):
        return "Hi {}".format(session["user"])"""
    if request.method == "POST":        #Only if data has been posted
        email=request.form.get('email')
        password=request.form.get('pass')
        try:
            #Try signing in the user with the given information
            user = auth.sign_in_with_email_and_password(email, password)
            #Insert the user data in the global person
            #session['user']=name
            """global person
            person["is_logged_in"] = True
            person["email"] = user["email"]
            person["uid"] = user["localId"]
            #Get the name of the user
            data = db.child("users").get()
            person["name"] = data.val()[person["uid"]]["name"]
            #Redirect to welcome page"""
            #return redirect(url_for('welcome'))
            return render_template("welcome.html")
        except:
            #If there is any error, redirect back to login
            #return "Your Email and Password Invalid Please Try login again or SignUp"
            return render_template("login.html",error="Your Email and Password Invalid Please Try login again or SignUp")
"""    else:
        if person["is_logged_in"] == True:
            return redirect(url_for('welcome'))
        else:
            return redirect(url_for('login'))
      

#If someone clicks on register, they are redirected to /register
@app.route("/register", methods = ["POST", "GET"])
def register():
    if request.method == "POST":        #Only listen to POST
        result = request.form           #Get the data submitted
        email = result["email"]
        password = result["pass"]
        confpass = result["cpass"]
        try:
            #Try creating the user account using the provided data
            if(password==confpass):
                auth.create_user_with_email_and_password(email, password)
            #Login the user
            user = auth.sign_in_with_email_and_password(email, password)
            #Add data to global person
            global person
            person["is_logged_in"] = True
            person["email"] = user["email"]
            person["uid"] = user["localId"]
            #person["name"] = name
            #Append data to the firebase realtime database
            #data = {"name": name, "email": email}
            #db.child("users").child(person["uid"]).set(data)
            #Go to welcome page
            return redirect(url_for('welcome'))
        except:
            #If there is any error, redirect to register
            return redirect(url_for('register'))

    else:
        if person["is_logged_in"] == True:
            return redirect(url_for('welcome'))
        else:
           return redirect(url_for('login'))
"""
if __name__ == "__main__":
    app.run(debug=True)
