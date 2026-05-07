import streamlit as st
import requests

st.title("Voyage Analytics ML App")

option = st.sidebar.selectbox(
    "Choose Prediction",
    ["Churn", "Flight", "Gender", "Recommendation"]
)

# ---------------- CHURN PREDICTION ----------------

if option == "Churn":

    st.header("Churn Prediction")

    API_URL = "https://your-render-api.onrender.com/predict/churn"

    tenure = st.number_input("Tenure", min_value=0)
    monthly = st.number_input("Monthly Charges", min_value=0.0)

    if st.button("Predict Churn"):

        data = {
            "tenure": tenure,
            "MonthlyCharges": monthly
        }

        response = requests.post(API_URL, json=data)

        st.write(response.json())


# ---------------- FLIGHT PREDICTION ----------------

elif option == "Flight":

    st.header("Flight Price Prediction")

    API_URL = "https://your-render-api.onrender.com/predict/flight"

    airline = st.text_input("Airline")
    source = st.text_input("Source")
    destination = st.text_input("Destination")
    total_stops = st.number_input("Total Stops", min_value=0)

    if st.button("Predict Flight Price"):

        data = {
            "airline": airline,
            "source": source,
            "destination": destination,
            "total_stops": total_stops
        }

        response = requests.post(API_URL, json=data)

        st.write(response.json())


# ---------------- GENDER PREDICTION ----------------

elif option == "Gender":

    st.header("Gender Prediction")

    API_URL = "https://your-render-api.onrender.com/predict/gender"

    name = st.text_input("Enter Name")

    if st.button("Predict Gender"):

        data = {
            "name": name
        }

        response = requests.post(API_URL, json=data)

        st.write(response.json())


# ---------------- RECOMMENDATION SYSTEM ----------------

elif option == "Recommendation":

    st.header("Recommendation System")

    API_URL = "https://your-render-api.onrender.com/predict/recommend"

    user_id = st.number_input("User ID", min_value=0)

    if st.button("Get Recommendations"):

        data = {
            "user_id": user_id
        }

        response = requests.post(API_URL, json=data)

        st.write(response.json())