from flask import Flask,render_template,request,redirect,url_for,jsonify
from utils import heart_disease


app = Flask(__name__,template_folder="template")

@app.route('/')
def hello_flask():
    print("Welcome to heart disease diagnose prediction")
    return render_template("home.html")

@app.route('/heart_diagnose',methods= ["GET","POST"])
def predict():
    if request.method == "GET":
        print("We are using GET method")
        Age = request.args.get("Age")
        Sex  = request.args.get("Sex")
        Chest_pain_type= request.args.get("Chest_pain_type")
        BP = request.args.get("BP")
        Cholesterol =request.args.get("Cholesterol")
        FBS_over_120 =request.args.get("FBS_over_120")
        EKG_results= request.args.get("EKG_results")
        Max_HR= request.args.get("Max_HR")
        Exercise_angina= request.args.get("Exercise_angina")
        ST_depression= request.args.get("ST_depression")
        Slope_of_ST = request.args.get("Slope_of_ST")
        Number_of_vessels_fluro=request.args.get("Number_of_vessels_fluro")
        Thallium =request.args.get("Thallium")

        print("Age,Sex, Chest_pain_type, BP,Cholesterol,FBS_over_120,EKG_results,Max_HR,Exercise_angina,ST_depression,Slope_of_ST,Number_of_vessels_fluro,Thallium\n",
            Age,Sex, Chest_pain_type, BP,Cholesterol,FBS_over_120,EKG_results,
            Max_HR,Exercise_angina,ST_depression,Slope_of_ST,
            Number_of_vessels_fluro,Thallium )
        
        diagnose = heart_disease(Age,Sex, Chest_pain_type, BP,Cholesterol,FBS_over_120,
                    EKG_results,Max_HR,Exercise_angina,ST_depression,
                    Slope_of_ST,Number_of_vessels_fluro,Thallium)

        heart_diagnose = diagnose.predict_model()

        if heart_diagnose == [1]:
            response = "presence"
        else:
            response = "absence"
        

        return(render_template("home.html",prediction= response))

        
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5050)                                                     