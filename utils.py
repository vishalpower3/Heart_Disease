import pandas as pd
import numpy as np
import pickle 
import json
import config
import sklearn

class heart_disease():
    def __init__(self,Age,Sex, Chest_pain_type, BP,Cholesterol,FBS_over_120,
                 EKG_results,Max_HR,Exercise_angina,ST_depression,
                 Slope_of_ST,Number_of_vessels_fluro,Thallium):
                 self.Age = Age
                 self.Sex  = Sex
                 self.Chest_pain_type= Chest_pain_type
                 self.BP = BP
                 self.Cholesterol =Cholesterol
                 self.FBS_over_120 =FBS_over_120
                 self.EKG_results= EKG_results
                 self.Max_HR= Max_HR
                 self.Exercise_angina= Exercise_angina
                 self.ST_depression= ST_depression
                 self.Slope_of_ST = Slope_of_ST
                 self.Number_of_vessels_fluro=Number_of_vessels_fluro
                 self.Thallium =Thallium

    def load_saved_file(self):
        with open(config.MODEL_FILE_PATH,"rb") as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,"r") as f:
            self.project_data = json.load(f)

    def predict_model(self):
        self.load_saved_file()
        
        # print("sex is :",Sex)
        # Sex = self.project_data["Sex"][Sex]
        # print("sex is :",Sex)
        # Chest_pain_type = self.project_data["Chest_pain_type"][Chest_pain_type]
        # FBS_over_120 = self.project_data["FBS_over_120"][FBS_over_120]
        # Exercise_angina = self.project_data["Exercise_angina"][Exercise_angina]
        # Thallium = self.project_data["Thallium"][Thallium]
        # Slope_of_ST =self.project_data["Slope_of_ST"][Slope_of_ST]



        columns =len(self.project_data["Columns"])
        test_array = np.zeros(columns)

        test_array[0] = self.Age
        test_array[1] = self.project_data["Sex"][self.Sex]
        test_array[2] = self.project_data["Chest_pain_type"][self.Chest_pain_type]
        test_array[3] = self.BP
        test_array[4] = self.Cholesterol
        test_array[5] = self.FBS_over_120
        test_array[6] = self.EKG_results
        test_array[7] = self.Max_HR                     
        test_array[8] = self.project_data["Exercise_angina"][self.Exercise_angina]
        test_array[9] = self.ST_depression
        test_array[10] = self.project_data["Slope_of_ST"][self.Slope_of_ST]
        test_array[11] = self.Number_of_vessels_fluro
        test_array[12] = self.project_data["Thallium"][self.Thallium]

        print("test array :",test_array)

        heart_prediction = self.model.predict([[test_array]][0])
        if heart_prediction == [1]:
            response="presence"
        else:
            response="absent"

        print("The heart prediction is :",response)

        return heart_prediction

if __name__ == "__main__":
    obj = heart_disease()
    obj

        


    
