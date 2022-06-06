from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("flight_rf.pkl", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Date_of_Journey
        date_dep = request.form["Dep_Time"]
        Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)
        # print("Journey Date : ",Journey_day, Journey_month)

        # Departure
        Dep_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)
        # print("Departure : ",Dep_hour, Dep_min)

        # Arrival
        date_arr = request.form["Arrival_Time"]
        Arrival_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)
        # print("Arrival : ", Arrival_hour, Arrival_min)

        # Duration
        dur_hour = abs(Arrival_hour - Dep_hour)
        dur_min = abs(Arrival_min - Dep_min)
        # print("Duration : ", dur_hour, dur_min)

        # Total Stops
        Total_stops = int(request.form["stops"])
        # print(Total_stops)

        # Airline
        airline=request.form['airline']
        if(airline=='Citilink'):
            Citilink = 1
            Sriwijaya_Air = 0
            Batik_Air = 0
            Lion_Air = 0
            Wings_Air = 0
            Garuda_Indonesia = 0
            Super_Air_Jet = 0
            Susi_Air = 0
            Air_Asia = 0

        elif (airline=='Sriwijaya Air'):
            Citilink = 0
            Sriwijaya_Air = 1
            Batik_Air = 0
            Lion_Air = 0
            Wings_Air = 0
            Garuda_Indonesia = 0
            Super_Air_Jet = 0
            Susi_Air = 0
            Air_Asia = 0

        elif (airline=='Batik Air'):
            Citilink = 0
            Sriwijaya_Air = 0
            Batik_Air = 1
            Lion_Air = 0
            Wings_Air = 0
            Garuda_Indonesia = 0
            Super_Air_Jet = 0
            Susi_Air = 0
            Air_Asia = 0
            
        elif (airline=='Lion Air'):
            Citilink = 0
            Sriwijaya_Air = 0
            Batik_Air = 0
            Lion_Air = 1
            Wings_Air = 0
            Garuda_Indonesia = 0
            Super_Air_Jet = 0
            Susi_Air = 0
            Air_Asia = 0
            
        elif (airline=='Wings Air'):
            Citilink = 0
            Sriwijaya_Air = 0
            Batik_Air = 0
            Lion_Air = 0
            Wings_Air = 1
            Garuda_Indonesia = 0
            Super_Air_Jet = 0
            Susi_Air = 0
            Air_Asia = 0
            
        elif (airline=='Garuda Indonesia'):
            Citilink = 0
            Sriwijaya_Air = 0
            Batik_Air = 0
            Lion_Air = 0
            Wings_Air = 0
            Garuda_Indonesia = 1
            Super_Air_Jet = 0
            Susi_Air = 0
            Air_Asia = 0

        elif (airline=='Super Air Jet'):
            Citilink = 0
            Sriwijaya_Air = 0
            Batik_Air = 0
            Lion_Air = 0
            Wings_Air = 0
            Garuda_Indonesia = 0
            Super_Air_Jet = 1
            Susi_Air = 0
            Air_Asia = 0

        elif (airline=='Susi Air'):
            Citilink = 0
            Sriwijaya_Air = 0
            Batik_Air = 0
            Lion_Air = 0
            Wings_Air = 0
            Garuda_Indonesia = 0
            Super_Air_Jet = 0
            Susi_Air = 1
            Air_Asia = 0

        elif (airline=='Air Asia'):
            Citilink = 0
            Sriwijaya_Air = 0
            Batik_Air = 0
            Lion_Air = 0
            Wings_Air = 0
            Garuda_Indonesia = 0
            Super_Air_Jet = 0
            Susi_Air = 0
            Air_Asia = 1

        else:
            Citilink = 0
            Sriwijaya_Air = 0
            Batik_Air = 0
            Lion_Air = 0
            Wings_Air = 0
            Garuda_Indonesia = 0
            Super_Air_Jet = 0
            Susi_Air = 0
            Air_Asia = 0

        # print(Citilink = 0
        # Sriwijaya_Air = 0
        # Batik_Air = 0
        # Lion_Air = 0
        # Wings_Air = 0
        # Garuda_Indonesia = 0
        # Super_Air_Jet = 1
        # Susi_Air = 0
        # Air_Asia = 0)

        Source = request.form["Source"]
        if (Source == 'Banyuwangi'):
            s_Banyuwangi = 1
            s_Yogyakarta = 0
            s_Surabaya = 0
            s_Malang = 0
            s_Jakarta = 0
            s_Semarang = 0
            s_Solo = 0
            s_Cilacap = 0
            s_Karimunjawa = 0

        elif (Source == 'Yogyakarta'):
            s_Banyuwangi = 0
            s_Yogyakarta = 1
            s_Surabaya = 0
            s_Malang = 0
            s_Jakarta = 0
            s_Semarang = 0
            s_Solo = 0
            s_Cilacap = 0
            s_Karimunjawa = 0

        elif (Source == 'Surabaya'):
            s_Banyuwangi = 0
            s_Yogyakarta = 0
            s_Surabaya = 1
            s_Malang = 0
            s_Jakarta = 0
            s_Semarang = 0
            s_Solo = 0
            s_Cilacap = 0
            s_Karimunjawa = 0

        elif (Source == 'Malang'):
            s_Banyuwangi = 0
            s_Yogyakarta = 0
            s_Surabaya = 0
            s_Malang = 1
            s_Jakarta = 0
            s_Semarang = 0
            s_Solo = 0
            s_Cilacap = 0
            s_Karimunjawa = 0
        
        elif (Source == 'Jakarta'):
            s_Banyuwangi = 0
            s_Yogyakarta = 0
            s_Surabaya = 0
            s_Malang = 0
            s_Jakarta = 1
            s_Semarang = 0
            s_Solo = 0
            s_Cilacap = 0
            s_Karimunjawa = 0
        
        elif (Source == 'Semarang'):
            s_Banyuwangi = 0
            s_Yogyakarta = 0
            s_Surabaya = 0
            s_Malang = 0
            s_Jakarta = 0
            s_Semarang = 1
            s_Solo = 0
            s_Cilacap = 0
            s_Karimunjawa = 0
        
        elif (Source == 'Solo'):
            s_Banyuwangi = 0
            s_Yogyakarta = 0
            s_Surabaya = 0
            s_Malang = 0
            s_Jakarta = 0
            s_Semarang = 0
            s_Solo = 1
            s_Cilacap = 0
            s_Karimunjawa = 0
        
        elif (Source == 'Cilacap'):
            s_Banyuwangi = 0
            s_Yogyakarta = 0
            s_Surabaya = 0
            s_Malang = 0
            s_Jakarta = 0
            s_Semarang = 0
            s_Solo = 0
            s_Cilacap = 1
            s_Karimunjawa = 0
        
        elif (Source == 'Karimunjawa'):
            s_Banyuwangi = 0
            s_Yogyakarta = 0
            s_Surabaya = 0
            s_Malang = 0
            s_Jakarta = 0
            s_Semarang = 0
            s_Solo = 0
            s_Cilacap = 0
            s_Karimunjawa = 1

        else:
            s_Banyuwangi = 0
            s_Yogyakarta = 0
            s_Surabaya = 0
            s_Malang = 0
            s_Jakarta = 0
            s_Semarang = 0
            s_Solo = 0
            s_Cilacap = 0
            s_Karimunjawa = 0

        Source = request.form["Destination"]
        if (Source == 'Jakarta'):
            d_Jakarta = 1
            d_Bandung = 0
            d_Semarang = 0
            d_Yogyakarta = 0
            d_Sidoarjo = 0
            d_Malang = 0
            d_Tangerang = 0
            d_Solo = 0
            d_Surabaya = 0
            d_Banyuwangi = 0
            d_Jawa_Barat = 0
            d_Jawa_Tengah = 0
        
        elif (Source == 'Bandung'):
            d_Jakarta = 0
            d_Bandung = 1
            d_Semarang = 0
            d_Yogyakarta = 0
            d_Sidoarjo = 0
            d_Malang = 0
            d_Tangerang = 0
            d_Solo = 0
            d_Surabaya = 0
            d_Banyuwangi = 0
            d_Jawa_Barat = 0
            d_Jawa_Tengah = 0

        elif (Source == 'Semarang'):
            d_Jakarta = 0
            d_Bandung = 0
            d_Semarang = 1
            d_Yogyakarta = 0
            d_Sidoarjo = 0
            d_Malang = 0
            d_Tangerang = 0
            d_Solo = 0
            d_Surabaya = 0
            d_Banyuwangi = 0
            d_Jawa_Barat = 0
            d_Jawa_Tengah = 0

        elif (Source == 'Yogyakarta'):
            d_Jakarta = 0
            d_Bandung = 0
            d_Semarang = 0
            d_Yogyakarta = 1
            d_Sidoarjo = 0
            d_Malang = 0
            d_Tangerang = 0
            d_Solo = 0
            d_Surabaya = 0
            d_Banyuwangi = 0
            d_Jawa_Barat = 0
            d_Jawa_Tengah = 0

        elif (Source == 'Sidoarjo'):
            d_Jakarta = 0
            d_Bandung = 0
            d_Semarang = 0
            d_Yogyakarta = 0
            d_Sidoarjo = 1
            d_Malang = 0
            d_Tangerang = 0
            d_Solo = 0
            d_Surabaya = 0
            d_Banyuwangi = 0
            d_Jawa_Barat = 0
            d_Jawa_Tengah = 0
        
        elif (Source == 'Malang'):
            d_Jakarta = 0
            d_Bandung = 0
            d_Semarang = 0
            d_Yogyakarta = 0
            d_Sidoarjo = 0
            d_Malang = 1
            d_Tangerang = 0
            d_Solo = 0
            d_Surabaya = 0
            d_Banyuwangi = 0
            d_Jawa_Barat = 0
            d_Jawa_Tengah = 0
        
        elif (Source == 'Tangerang'):
            d_Jakarta = 0
            d_Bandung = 0
            d_Semarang = 0
            d_Yogyakarta = 0
            d_Sidoarjo = 0
            d_Malang = 0
            d_Tangerang = 1
            d_Solo = 0
            d_Surabaya = 0
            d_Banyuwangi = 0
            d_Jawa_Barat = 0
            d_Jawa_Tengah = 0
        
        elif (Source == 'Solo'):
            d_Jakarta = 0
            d_Bandung = 0
            d_Semarang = 0
            d_Yogyakarta = 0
            d_Sidoarjo = 0
            d_Malang = 0
            d_Tangerang = 0
            d_Solo = 1
            d_Surabaya = 0
            d_Banyuwangi = 0
            d_Jawa_Barat = 0
            d_Jawa_Tengah = 0
        
        elif (Source == 'Surabaya'):
            d_Jakarta = 0
            d_Bandung = 0
            d_Semarang = 0
            d_Yogyakarta = 0
            d_Sidoarjo = 0
            d_Malang = 0
            d_Tangerang = 0
            d_Solo = 0
            d_Surabaya = 1
            d_Banyuwangi = 0
            d_Jawa_Barat = 0
            d_Jawa_Tengah = 0
        
        elif (Source == 'Banyuwangi'):
            d_Jakarta = 0
            d_Bandung = 0
            d_Semarang = 0
            d_Yogyakarta = 0
            d_Sidoarjo = 0
            d_Malang = 0
            d_Tangerang = 0
            d_Solo = 0
            d_Surabaya = 0
            d_Banyuwangi = 1
            d_Jawa_Barat = 0
            d_Jawa_Tengah = 0
        
        elif (Source == 'Jawa Barat'):
            d_Jakarta = 0
            d_Bandung = 0
            d_Semarang = 0
            d_Yogyakarta = 0
            d_Sidoarjo = 0
            d_Malang = 0
            d_Tangerang = 0
            d_Solo = 0
            d_Surabaya = 0
            d_Banyuwangi = 0
            d_Jawa_Barat = 1
            d_Jawa_Tengah = 0
        
        elif (Source == 'Jawa Tengah'):
            d_Jakarta = 0
            d_Bandung = 0
            d_Semarang = 0
            d_Yogyakarta = 0
            d_Sidoarjo = 0
            d_Malang = 0
            d_Tangerang = 0
            d_Solo = 0
            d_Surabaya = 0
            d_Banyuwangi = 0
            d_Jawa_Barat = 0
            d_Jawa_Tengah = 1
        
        else:
            d_Jakarta = 0
            d_Bandung = 0
            d_Semarang = 0
            d_Yogyakarta = 0
            d_Sidoarjo = 0
            d_Malang = 0
            d_Tangerang = 0
            d_Solo = 0
            d_Surabaya = 0
            d_Banyuwangi = 0
            d_Jawa_Barat = 0
            d_Jawa_Tengah = 0
        

    #     ['Total_Stops', 'Journey_day', 'Journey_month', 'Dep_hour',
    #    'Dep_min', 'Arrival_hour', 'Arrival_min', 'Duration_hours',
    #    'Duration_mins', 'Airline_Air India', 'Airline_GoAir', 'Airline_IndiGo',
    #    'Airline_Jet Airways', 'Airline_Jet Airways Business',
    #    'Airline_Multiple carriers',
    #    'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet',
    #    'Airline_Trujet', 'Airline_Vistara', 'Airline_Vistara Premium economy',
    #    'Source_Chennai', 'Source_Delhi', 'Source_Kolkata', 'Source_Mumbai',
    #    'Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad',
    #    'Destination_Kolkata', 'Destination_New Delhi']
        
        prediction=model.predict([[
            Total_stops,
            Journey_day,
            Journey_month,
            Dep_hour,
            Dep_min,
            Arrival_hour,
            Arrival_min,
            dur_hour,
            dur_min,
            Citilink,
            Sriwijaya_Air,
            Batik_Air,
            Lion_Air,
            Wings_Air,
            Garuda_Indonesia,
            Super_Air_Jet,
            Susi_Air,
            Air_Asia,
            s_Banyuwangi,
            s_Yogyakarta,
            s_Surabaya,
            s_Malang,
            s_Jakarta,
            s_Semarang,
            s_Solo,
            s_Cilacap,
            s_Karimunjawa,
            d_Jakarta,
            d_Bandung,
            d_Semarang,
            d_Yogyakarta,
            d_Sidoarjo,
            d_Malang,
            d_Tangerang,
            d_Solo,
            d_Surabaya,
            d_Banyuwangi,
            d_Jawa_Barat,
            d_Jawa_Tengah
        ]])

        output=round(prediction[0],2)

        return render_template('home.html',prediction_text="Your Flight price is Rp. {}".format(output))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)
