
# from crypt import methods
from flask import Flask,render_template,request
app = Flask(__name__)#interface between webserver and web application


@app.route("/" , methods = ['GET','POST'])
def home():
    return render_template("registration.html")  

@app.route('/res',methods=['GET',"POST"])
def res():
    if request.method == "POST":
        firstname = request.form.get('firstname')
    return render_template('result1.html', fname=firstname)   




@app.route('/login/', methods=['GET',"POST"])
def ncd():
    return render_template('ncd.html')

@app.route('/result',methods=['GET',"POST"])
def result():
    if request.method == "POST":
        count = 0

# getting the value for age

        while True :
            try:
                age = request.form.get('age')
                if (int(age)>=30 and int(age)<=39):
                    count+= 0
                    break
                elif(int(age)>=40 and int(age)<=49):
                    count = count+1
                    break
                elif(int(age)>=50 and int(age)<=59):
                    count+=2
                    break
                elif (int(age)>=60):
                    count+=3
                    break
                else:
                    print("Enter the valid age")  
            except ValueError:
                continue
        
        while True:
            try:
                smoke = request.form.get('smoke')
                # if smoke in lis1:
                if (str(smoke).lower() == "never"):
                    count = count+0
                    break
                elif((str(smoke).lower() =="used to consume in past")or (str(smoke).lower() =="sometime now")):
                    count+=1
                    break
                elif (str(smoke).lower() =="daily"):
                    count+=2
                    break
                else:
                    print("Enter the valid result for smoking.")  
            except TypeError:
                continue
        while True:
            try:
                alcohol =request.form.get('alcohol')

                yes_choices = ['yes', 'y']
                no_choices = ['no', 'n']

                if (str(alcohol).lower() in yes_choices):
                    count  = count+0
                    break
                elif (str(alcohol).lower() in no_choices):
                    count = count+1
                    break
                else:
                    print("Give the alcohol choice")
                    break
            except TypeError:
                continue    

        while True:
            try:
                gender_m = request.form.get('male')
                gender_f = request.form.get('female')
                measurement = request.form.get('measurement')
                print(gender_m,gender_f,measurement)
                if(str(gender_m).lower() == "on"):
                    if (int(measurement)<=90):
                        count = count+0
                        break
                    elif (int(measurement)>90 and int( measurement)<=100):
                        count = count+1
                        break
                    elif (int(measurement)>100):
                        count+=2
                        break
                elif(str(gender_f).lower() == "on"):
                    if (int(measurement)<=80):
                        count = count+0
                        break
                    elif (int(measurement)>80 and int(measurement)<=90):
                        count = count+1
                        break
                    elif (int(measurement)>90):
                        count+=2    
                        break
                else:
                    print("Give the correct measurement input")
                    break
            except ValueError:
                continue

        while True:
            try:
                physical =  request.form.get('physical')


                if (int(physical)>=150):
                    count = count+0
                    break
                else:
                    count = count+1
                    break
            except ValueError:
                continue
        # print("count 5",count)

        while True:
            try:
                disease_family_hist =  request.form.get('fam')

                yes_choices = ['yes', 'y']
                no_choices = ['no', 'n']
                if (str(disease_family_hist).lower() in no_choices):
                    count = count+0
                    break
                elif (str(disease_family_hist).lower() in yes_choices):
                    count = count+2
                    break
                else:
                    print("give the correct family history disease input")
                    break
            except TypeError:
                continue
        add = count
        print(add)
        res=""
        if count>4:
            res="you need screening" 
        else:
            res="No screening needed"

        return render_template('result1.html', add1=add,prescription=res)
    return render_template('result1.html', add1="result not found in session.")

@app.route('/back',methods=['GET',"POST"])  
def back():  
    if request.method == 'POST':
        return render_template("ncd.html");  
if __name__ == '__main__':
    app.run(debug = True)  
    
