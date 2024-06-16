
# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
import pickle
import numpy as np

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
            #  reading the inputs given by the user
            Fare_class=int(request.form['Fare_class'])
            Passenger_count = int(request.form['Passenger_count'])
            Year = int(request.form['Year'])
            Month = int(request.form['Month'])
            Day = int(request.form['Day'])
            Hour = int(request.form['Hour'])
            Minutes = int(request.form['Minutes'])
            Part_of_day=int(request.form['Part_of_day'])
            Distance_Travelled=float(request.form['Distance_Travelled'])
            best_model=pickle.load(open("best_model1.pkl","rb"))
            total_inputs=[[Fare_class,Passenger_count,Year,Month,Day,Hour,Minutes,Part_of_day,Distance_Travelled]]

            prediction=best_model.predict(total_inputs)
            print('The Fare prediction for the trip is', prediction)
            # showing the prediction results in a UI
            return render_template('results.html',prediction=prediction[0])


if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True) # running the app