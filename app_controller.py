from analyzer_ui import *
from data_analysis import *
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from csv import writer
import pandas as pd


class AppController:

    def __init__(self):
        pass

    def ml(self, listt):
        features = ['BMI', 'Smoking', 'AlcoholDrinking', 'Stroke', 'DiffWalking', 'Sex', 'AgeCategory',
                    'Diabetic', 'PhysicalActivity', 'GenHealth', 'SleepTime',
                    'Asthma', 'KidneyDisease', 'SkinCancer']
        le = LabelEncoder()
        with open('heart_2020_cleaned.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(listt)
            f_object.close()
        temp_data = pd.read_csv('heart_2020_cleaned.csv')
        for feature in features:
            try:
                temp_data[feature] = le.fit_transform(temp_data[feature])
            except:
                print('Error encoding ' + feature)
        predict_list = list()
        tmp = temp_data.values.tolist()[len(temp_data) - 1]
        for i in range(len(tmp)):
            if tmp[i] != 'Null':
                predict_list.append(tmp[i])
        with open('heart_2020_cleaned.csv', 'r+') as filep:
            lines = filep.readlines()
            filep.seek(0)
            filep.truncate()
            filep.writelines(lines[:-1])
        temp_data = pd.read_csv('heart_2020_cleaned.csv')
        for feature in features:
            try:
                temp_data[feature] = le.fit_transform(temp_data[feature])
            except:
                print('Error encoding ' + feature)
        percenttrain = 0.85
        dataTrain, dataTest = train_test_split(
            temp_data, train_size=percenttrain, random_state=0)

        nb = GaussianNB()
        nb.fit(dataTrain[features], dataTrain['HeartDisease'])

        predictions = nb.predict(dataTest[features])
        accuracy = accuracy_score(dataTest['HeartDisease'], predictions)
        # print('Percent correct:', accuracy * 100, '%')
        a = nb.predict([predict_list])
        return a[0]


if __name__ == '__main__':
    data = DataAnalytic()
    ui = MyApp(data)
    ui.run()

