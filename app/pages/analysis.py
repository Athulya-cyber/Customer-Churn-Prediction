import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')


st.header("📊 Data Visualization")

st.subheader("Dataset")

st.write(
    "Download the Telco Customer Churn dataset from Kaggle "
    "and upload the CSV file below."
)

st.markdown(
    "[Download the Telco Customer Churn Dataset from Kaggle]"
    "(https://www.kaggle.com/datasets/blastchar/telco-customer-churn)"
)

uploaded_file = st.file_uploader(
    "Upload the Telco Customer Churn CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    data = pd.read_csv(uploaded_file)

    show_data = st.checkbox("Show Dataset")

    if show_data:
        st.dataframe(data, use_container_width=True)

    st.markdown("---")

    st.subheader("Dataset Overview")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Number of Records",
            data.shape[0]
        )

    with col2:
        st.metric(
            "Number of Features",
            data.shape[1]
        )

    st.markdown("---")

    st.subheader("📋 Column Details")

    column_details = {
        "customerID": "Unique identifier assigned to each customer.",
        "gender": "Gender of the customer.",
        "SeniorCitizen": "Indicates whether the customer is a senior citizen.",
        "Partner": "Indicates whether the customer has a partner.",
        "Dependents": "Indicates whether the customer has dependents.",
        "tenure": "Number of months the customer has stayed with the company.",
        "PhoneService": "Indicates whether the customer has phone service.",
        "MultipleLines": "Indicates whether the customer has multiple phone lines.",
        "InternetService": "Type of internet service used by the customer.",
        "OnlineSecurity": "Indicates whether the customer has online security service.",
        "OnlineBackup": "Indicates whether the customer has online backup service.",
        "DeviceProtection": "Indicates whether the customer has device protection service.",
        "TechSupport": "Indicates whether the customer has technical support service.",
        "StreamingTV": "Indicates whether the customer has streaming TV service.",
        "StreamingMovies": "Indicates whether the customer has streaming movie service.",
        "Contract": "Type of contract chosen by the customer.",
        "PaperlessBilling": "Indicates whether the customer uses paperless billing.",
        "PaymentMethod": "Payment method used by the customer.",
        "MonthlyCharges": "Monthly charges paid by the customer.",
        "TotalCharges": "Total charges accumulated by the customer.",
        "Churn": "Indicates whether the customer left the company."
    }

    column_df = pd.DataFrame(
        column_details.items(),
        columns=["Column", "Description"]
    )

    st.dataframe(column_df, use_container_width=True)

    st.markdown("---")

    st.subheader("Statistics")

    st.dataframe(data.describe())

    st.markdown("---")

    st.title("Data Analysis")

    # Churn Distribution
    st.subheader("Churn Distribution")

    fig = plt.figure(figsize=(6, 4))

    sns.countplot(data=data, x='Churn')

    plt.title('Customer Churn Distribution')
    plt.xlabel('Churn')
    plt.ylabel('Number of Customers')

    plt.close(fig)
    st.pyplot(fig)

    st.markdown("---")

    # Churn by Contract Type
    st.subheader("Churn by Contract Type")

    fig = plt.figure(figsize=(8, 5))

    sns.countplot(
        data=data,
        x='Contract',
        hue='Churn'
    )

    plt.title('Customer Churn by Contract Type')
    plt.xlabel('Contract Type')
    plt.ylabel('Number of Customers')
    plt.legend(title='Churn')

    plt.close(fig)
    st.pyplot(fig)

    st.markdown("---")

    # Churn by Internet Service
    st.subheader("Churn by Internet Service")

    fig = plt.figure(figsize=(8, 5))

    sns.countplot(
        data=data,
        x='InternetService',
        hue='Churn'
    )

    plt.title('Customer Churn by Internet Service')
    plt.xlabel('Internet Service')
    plt.ylabel('Number of Customers')
    plt.legend(title='Churn')

    plt.close(fig)
    st.pyplot(fig)

    st.markdown("---")

    # Churn by Payment Method
    st.subheader("Churn by Payment Method")

    fig = plt.figure(figsize=(10, 5))

    sns.countplot(
        data=data,
        x='PaymentMethod',
        hue='Churn'
    )

    plt.title('Customer Churn by Payment Method')
    plt.xlabel('Payment Method')
    plt.ylabel('Number of Customers')
    plt.legend(title='Churn')

    plt.close(fig)
    st.pyplot(fig)

    st.markdown("---")

    # Tenure vs Churn
    st.subheader("Tenure vs Churn")

    fig = plt.figure(figsize=(8, 5))

    sns.boxplot(
        data=data,
        x='Churn',
        y='tenure'
    )

    plt.title('Tenure Distribution by Churn')
    plt.xlabel('Churn')
    plt.ylabel('Tenure (Months)')

    plt.close(fig)
    st.pyplot(fig)

    st.markdown("---")

    # Monthly Charges vs Churn
    st.subheader("Monthly Charges vs Churn")

    fig = plt.figure(figsize=(8, 5))

    sns.boxplot(
        data=data,
        x='Churn',
        y='MonthlyCharges'
    )

    plt.title('Monthly Charges Distribution by Churn')
    plt.xlabel('Churn')
    plt.ylabel('Monthly Charges')

    plt.close(fig)
    st.pyplot(fig)

    st.markdown("---")

    # Total Charges vs Churn
    st.subheader("Total Charges vs Churn")

    fig = plt.figure(figsize=(8, 5))

    sns.boxplot(
        data=data,
        x='Churn',
        y='TotalCharges'
    )

    plt.title('Total Charges Distribution by Churn')
    plt.xlabel('Churn')
    plt.ylabel('Total Charges')

    plt.close(fig)
    st.pyplot(fig)

    st.markdown("---")

    st.subheader("🔍 Key Insights")

    st.markdown("""
    - The dataset contains customers who both **churned and did not churn**.
    - Customers with **month-to-month contracts** account for a large number of churned customers.
    - **Fiber optic** customers show a high number of churned customers.
    - **Electronic check** is associated with a high number of churned customers.
    - Churned customers generally have **shorter tenure**.
    - Churned customers generally show **higher monthly charges**.
    - Non-churned customers generally have **higher total charges**, which may be related to their longer tenure.
    """)

else:

    st.info(
        "Please upload the Telco Customer Churn CSV file above "
        "to view the dataset analysis."
    )
