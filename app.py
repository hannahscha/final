import streamlit as st
import numpy as np
import pandas as pd
from sklearn.externals import joblib  # If you're using a saved model

# Load your trained model (replace 'model.pkl' with your model's file path)
model = joblib.load('random_forest_model.pkl')

# Define input fields for the user
st.title("Specific Capacitance Prediction for BAC Electrodes")

# Collect inputs from the user
material = st.selectbox("Material", ['Willow', 'Orange peel', 'Loofah sponge', 'Pine nut shell', 'Gelatin'])
doping_agent = st.text_input("Doping Agent", '')
activation_agent = st.selectbox("Activation Agent", ['KOH', 'NaOH', 'H3PO4'])
ratio_activation_agent = st.number_input("Ratio of Activation Agent", min_value=0.0, max_value=5.0, value=1.0)
pre_carbonization_temp = st.number_input("Pre Carbonization Temperature (°C)", min_value=0, max_value=1000, value=500)
time_h = st.number_input("Time (h)", min_value=0.0, max_value=10.0, value=2.0)
carbonization_temp = st.number_input("Carbonization Temperature (°C)", min_value=0, max_value=1000, value=700)
carbonization_time = st.number_input("Carbonization Time (h)", min_value=0.0, max_value=10.0, value=2.0)
acr = st.number_input("ACR (%)", min_value=0.0, max_value=100.0, value=80.0)
cmr = st.number_input("CMR (%)", min_value=0.0, max_value=100.0, value=20.0)
br = st.number_input("BR (%)", min_value=0.0, max_value=100.0, value=10.0)
kb = st.number_input("KB", min_value=0.0, max_value=10.0, value=1.0)
cm_ac = st.number_input("CM/AC", min_value=0.0, max_value=10.0, value=1.0)
b_ac = st.number_input("B/AC", min_value=0.0, max_value=10.0, value=1.0)
cm_b = st.number_input("CM/B", min_value=0.0, max_value=10.0, value=1.0)
v0_1 = st.number_input("V0.1 (cm^3/g)", min_value=0.0, max_value=1000.0, value=200.0)
v0_4 = st.number_input("V0.4 (cm^3/g)", min_value=0.0, max_value=1000.0, value=300.0)
v0_9 = st.number_input("V0.9 (cm^3/g)", min_value=0.0, max_value=1000.0, value=350.0)
purifying = st.text_input("Purifying", 'diluted HCl + water')
molarity_hcl = st.number_input("Molarity of HCl (M)", min_value=0.0, max_value=10.0, value=1.0)
electrode_system = st.selectbox("Electrode system (2E/3E)", ['2E', '3E'])
molarity_electrolyte = st.number_input("Molarity of Electrolyte (M)", min_value=0.0, max_value=10.0, value=6.0)
electrolyte_kind = st.selectbox("Electrolyte Kind", ['KOH', 'H2SO4'])
potential_window = st.number_input("Potential Window (V)", min_value=0.0, max_value=10.0, value=1.0)

# Prepare the input data as a dataframe
input_data = pd.DataFrame({
    'Material': [material],
    'Doping Agent': [doping_agent],
    'Activation Agent': [activation_agent],
    'Ratio of activation Agent': [ratio_activation_agent],
    'pre carbonization (°C)': [pre_carbonization_temp],
    'Time (h)': [time_h],
    'Carbonization (°C)': [carbonization_temp],
    'Time (h).1': [carbonization_time],
    'ACR (%)': [acr],
    'CMR (%)': [cmr],
    'BR (%)': [br],
    'KB': [kb],
    'CM/AC': [cm_ac],
    'B/AC': [b_ac],
    'CM/B': [cm_b],
    'V0.1 (cm^3/g)': [v0_1],
    'V0.4 (cm^3/g)': [v0_4],
    'V0.9 (Cm^3/g)': [v0_9],
    'Purifying': [purifying],
    'Molarity of HCl (M)': [molarity_hcl],
    'Electrode system (2E/3E)': [electrode_system],
    'Molarity of Electrolyte (M)': [molarity_electrolyte],
    'Electrolyte Kind': [electrolyte_kind],
    'Potential Window (V)': [potential_window]
})

# Preprocess input data
input_preprocessed = preprocessor.transform(input_data)

# Predict specific capacitance
predicted_capacitance = model.predict(input_preprocessed)

# Display prediction
st.write(f"Predicted Specific Capacitance (F/g): {predicted_capacitance[0]:.2f}")
