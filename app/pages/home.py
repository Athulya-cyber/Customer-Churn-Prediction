import streamlit as st

st.title("👥📉 Customer Churn Prediction")

st.header("Customer Churn Prediction using SVM Classifier")

st.write("""
Customer churn occurs when a customer stops using a company's products or services.

For subscription-based businesses such as telecommunications companies, 
understanding and predicting customer churn can support customer retention 
and data-driven business decisions.
""")

st.subheader("📊 About the Dataset")

st.write("""
This project uses the **Telco Customer Churn dataset**, which contains 
customer demographic information, subscribed services, contract details, 
and billing information.

The target variable, **Churn**, indicates whether a customer has left the company.
""")

st.subheader("🤖 Project Objective")

st.write("""
The objective is to develop a **Support Vector Machine (SVM)** classification 
model to predict whether a customer is likely to **churn or remain with the company**.
""")

st.info("Use the navigation menu on the left to explore each section.")
