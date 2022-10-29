from flask import Flask,render_template,request
from pymongo import MongoClient

# import json
app = Flask(__name__)#interface between webserver and web application



firstname = " "
add = 0
result = " "

@app.route("/" , methods = ['GET','POST'])
def home():
    return render_template("registration.html")
    # def create_user():
    # try:
    #     user = {"name":request.form['fname'],
    #     "lastname":request.form['lname'],
    #     "email":request.form['email'],
    #     "gender":request.form['gender'],
    #     "pincode":request.form["pincode"]
    #     }
    #     dbResponse = db.users.insert_one(user)
    #     print (dbResponse.inserted_id)
    #     return Response(
    #         response = json.dumps(
    #             {"message":"user created",
    #             "id":f"{dbResponse.inserted_id}"
    #             }
    #         ),
    #         status = 200,
    #         mimetype = "application/json"
    #         )
    # except Exception as e:
    #     print(e)
      

# route to get data from html form and insert data into database
@app.route('/registration', methods=["GET", "POST"])
def registration():
    global firstname
    middlename = " "
    lastname = " "
    email = " "
    gender = " "
    birthday = " "
    pincode = " "
    if request.method == "POST":
    
        firstname = request.form['fname']
        middlename = request.form['mname']
        lastname = request.form['lname']
        email =  request.form['email']
        gender = request.form['gender']
        birthday = request.form['birthday']
        pincode = request.form["pincode"]
        
        Collection.insert_one(
            {"firstname" : firstname,
        'middlename': middlename,
        "lastname":lastname,
        "email":email,
        "gender":gender,
        "birthday":birthday,
        "pincode":pincode}
        )
    # print(data)
    return render_template("ncd1.html",fname = firstname,mname= middlename,lname =  lastname,email1 = email,gender1 = gender,birthday1 = birthday,pincode1 = pincode)


@app.route('/res',methods=['GET',"POST"])
def res():
    # if request.method == "POST":
        # firstname = request.form.get('firstname')
    return render_template('result1.html')   




@app.route('/login/', methods=['GET',"POST"])
def login():
    # data = {}
    # if request.method == "POST":
         
    #     data['firstname']=  request.form['fname']    
    #     data['middlename'] = request.form['mname']
    #     data['lastname'] = request.form['lname']
    #     data['email'] = request.form['email']
    #     data['gender'] = request.form['gender']
    #     data['birthday'] = request.form['birthday']
    #     data['pincode'] = request.form["pincode"]
    #     Collection.insert_one(data)
       
            # data['middlename'] = request.form['mname']
        # data['lastname'] = request.form['lname']
        # data['email'] = request.form['email']
        # data['gender'] = request.form['gender']
        # data['birthday'] = request.form['birthday']
        # data['pincode'] = request.form["pincode"]
        # }
    
    
    return render_template('ncd1.html')

@app.route('/result',methods=['GET',"POST"])
def result():
    if request.method == "POST":
        count = 0

# getting the value for age

        while True :
            age = ""
            smoke = ""
            alcohol = ""
            measurement = ""
            physical = ""
            disease_family_hist = ""
        
            age = request.form['age']
            
            smoke = request.form['smoke']
            
            alcohol =request.form['alcohol']

            
            measurement = request.form['measurement']
            
            physical =  request.form['physical']



            disease_family_hist =  request.form['history']
        
            # age = request.form.get('age')
            
            # smoke = request.form.get('smoke')
            
            # alcohol =request.form.get('alcohol')
            # measurement = request.form.get('measurement')
            
            # physical =  request.form.get('physical')



            # disease_family_hist =  request.form.get('history')
            Collection.update_one(
                {"firstname":firstname},
                
            {"$set": {"age" :age,
        'smoke': smoke,
        "alcohol":alcohol,
        "measurement":measurement,
        "physical":physical,
        
        "disease_family_hist":disease_family_hist}}
       
        )
        
            count = int(age)+int(smoke)+int(alcohol)+int(measurement)+int(physical)+int(disease_family_hist)
            
            global add 
            add = count
            print(add)
            global result
            if count>4:
                result="you need screening" 
                Collection.update_one(
                {"firstname":firstname},
                {"$set": {"total_count" :add,"result" :result}})
            else:
                result="No screening needed"
                Collection.update_one(
                {"firstname":firstname},{"$set": {"total_count" :add,"result" :result}})


            return render_template('result1.html', add1=add,prescription=result)
    return render_template('result1.html', add1="result not found in session.")

@app.route('/back',methods=['GET',"POST"])  
def back():  
    if request.method == 'POST':
        return render_template("ncd1.html");  

        
if __name__ == '__main__':

    try:
        client = MongoClient("mongodb://localhost:27017")
        db = client['patientData']
        Collection = db["mysamecollectionforpatient"]
        # client.server_info() #trigger exception if it cannot connect to database
        
    except Exception as e:
        print(e)
        print("Error - Cannot connect to database")

    # print(data.fname)
    app.run(debug=True)