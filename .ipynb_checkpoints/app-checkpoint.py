import streamlit as st
import joblib
import numpy as np
import pandas as pd

model = joblib.load("customer_churn_rf.pkl")
st.set_page_config(
    page_title="Customer Churn Prediction",
    layout="wide"
)

st.markdown(
    "<h1 style='color:orange;text-align:center'>Customer Churn Prediction</h1>",
    unsafe_allow_html=True
)

col1,col2=st.columns(2)
with col1:
    account_length = st.number_input("Account Length")
    number_vmail_messages = st.number_input(
        "Number of Voicemail Messages"
    )
    
    total_day_minutes = st.number_input(
        "Total Day Minutes"
    )
    

with col2:
       total_eve_minutes = st.number_input(
        "Total Evening Minutes"
       )
       total_night_minutes = st.number_input(
        "Total Night Minutes"
        )
    
       total_intl_minutes = st.number_input(
        "Total International Minutes"
        )

st.sidebar.title("Customer Information")
international_plan = st.sidebar.selectbox(
    "International Plan",
    [0,1])
voice_mail_plan = st.sidebar.selectbox(
"Voice mail Plan",
[0,1])


customer_service_calls = st.number_input(
    "Customer Service Calls"
)
total_calls = st.number_input(
    "Total Calls"
)

intl_plan_heavy_user = (
    1 if international_plan == 1 and total_intl_minutes > 10 else 0
)


total_minutes=(
    total_day_minutes
    +total_eve_minutes
    +total_night_minutes
    +total_intl_minutes
)
average_call_duration = (total_minutes / total_calls
                         if total_calls != 0 else 0)

day_usage_ratio = (
    total_day_minutes / total_minutes
    if total_minutes != 0 else 0
)

intl_usage_ratio = (
    total_intl_minutes / total_minutes
    if total_minutes != 0 else 0
)
high_complaint = (
    1 if customer_service_calls > 3 else 0
)


calls_per_day = (
    total_calls / account_length
    if account_length != 0 else 0
)


# Predict
st.markdown("""
<style>
div.stButton > button:first-child {
    display:flex;
    justify-content:center;
    align-item:center;
    width: 40vw;
    background-color: teal;
    color: white;
    height: 3em;
    border-radius: 10px;
    font-size: 20px;
    border: none;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1,2,1])

with col2:
    predict = st.button("Predict")

if predict:

    features = np.array([[
        account_length,
        international_plan,
        voice_mail_plan,
        number_vmail_messages,
        total_day_minutes,
        total_eve_minutes,
        total_night_minutes,
        total_intl_minutes,
        customer_service_calls,
        total_minutes,
        total_calls,
        average_call_duration,
        day_usage_ratio,
        intl_usage_ratio,
        high_complaint,
        calls_per_day,
        intl_plan_heavy_user
    ]])

    prediction = model.predict(features)
    probability = model.predict_proba(features)

    churn_prob = probability[0][1] * 100

    if prediction[0] == 1:
        st.error("Customer May Churn")
    else:
        st.success("Customer Will Stay")

    st.metric(
        label="Churn Probability",
        value=f"{churn_prob:.2f}%"
    )







