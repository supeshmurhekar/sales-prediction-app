import streamlit as st
import pandas as pd
import pickle
# load model and columns 
model = pickle.load(open("sales_model.pkl","rb"))
cols = pickle.load(open("columns.pkl","rb"))
st.title("Sales Predication App")
st.write("This app predicts sales based on marketing spend.")
# inputs
tv = st.number_input("TV Spend", min_value=0)
digital = st.number_input("Digital Spend",min_value=0)
influencer = st.number_input("Influencer Spend",min_value=0)
discount = st.number_input("Discount",min_value=0)
visits = st.number_input("Website Visits",min_value=0)
leads = st.number_input("Leads",min_value=0)
conversion = st.number_input("Conversion Rate",min_value=0)


# predict 
if st.button("Predict Sales"):

    input_data = pd.DataFrame(columns=cols)
    input_data.loc[0] = 0

    input_data['TV_Spend'] = tv
    input_data['Digital_Spend'] = digital
    input_data['Influencer_Spend'] = influencer
    input_data['Discount'] = discount
    input_data['Website_Visits'] = visits
    input_data['Leads'] = leads
    input_data['Conversion_Rate'] = conversion

    # prediction = model.predict(input_data)
    # prediction = max(0, prediction[0])

    # st.success(f"Predicted Sales: ₹ {round(prediction, 2)}")
    prediction = model.predict(input_data)
    st.write("Raw Prediction:", prediction[0])   # 👈 ADD THIS
    prediction = max(0, prediction[0])
    st.success(f"Predicted Sales: ₹ {round(prediction, 2)}")
