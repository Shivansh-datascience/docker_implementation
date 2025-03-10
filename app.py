from flask import Flask , render_template , jsonify 
from flask import request 

#creating an flask API 
app = Flask(__name__)

#directing the each function with for running the html file in one server
@app.route(rule="/",methods=['GET'])
def run_html_page():
    return render_template("login.html")

#getting the users credentials from html file
@app.route(rule="/users_credentials",methods=['GET'])
def get_credentials():
    try:
        username = request.form.get("Username")  #getting the credentials for username 
        Password = request.form.get("Password")  #getting the credentials for password
        if not username or not Password:
            return jsonify({"missing username and password"},400)
    except Exception as e:
        return {"error": str(e)}, 500 
    finally:
        return jsonify({"username":username,"password":Password})
    

    
#calling the api server with host and port number
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=6065)

