import streamlit as st
import pandas as pd
import joblib

# Ladda tränad modell
model = joblib.load("car_price_model.pkl")

# Titel
st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>Car Price Predictor</h1>", unsafe_allow_html=True)
st.write("Predict the estimated price of a car based on its features.")

# Sidebar för alla bilattribut
st.sidebar.header("Car Details")
brands = ["Toyota", "BMW", "Ford", "Honda"]
models = ["Corolla", "3 Series", "Focus", "Civic"]
years = list(range(1990, 2026))
engine_sizes = [0.8, 1.0, 1.2, 1.5, 2.0, 2.5, 3.0, 4.0]
fuels = ["Petrol", "Diesel", "Hybrid", "Electric"]
transmissions = ["Manual", "Automatic"]
doors_options = [2, 3, 4, 5]
owner_counts = [1, 2, 3, 4, 5]

brand = st.sidebar.selectbox("Brand", brands)
model_name = st.sidebar.selectbox("Model", models)
year = st.sidebar.selectbox("Year of Manufacture", years)
engine = st.sidebar.selectbox("Engine Size (L)", engine_sizes)
fuel = st.sidebar.selectbox("Fuel Type", fuels)
transmission = st.sidebar.selectbox("Transmission", transmissions)
doors = st.sidebar.selectbox("Number of Doors", doors_options)
owner_count = st.sidebar.selectbox("Number of Previous Owners", owner_counts)
mileage = st.sidebar.number_input("Mileage (km)", 0, 500000, 50000, step=1000)

# Snygg knapp centrerad
st.markdown("<h3 style='text-align: center;'>Predict Your Car Price</h3>", unsafe_allow_html=True)
predict_button = st.button("Predict Price")

# Prediktion och snygg output
if predict_button:
    input_data = pd.DataFrame({
        "Brand": [brand],
        "Model": [model_name],
        "Year": [year],
        "Engine_Size": [engine],
        "Fuel_Type": [fuel],
        "Transmission": [transmission],
        "Mileage": [mileage],
        "Doors": [doors],
        "Owner_Count": [owner_count]
    })

    prediction = model.predict(input_data)

    st.markdown("### Estimated Car Price")
    st.metric(label=f"{brand} {model_name} ({year})", value=f"${prediction[0]:,.0f}")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>Made with Streamlit</p>", unsafe_allow_html=True)
