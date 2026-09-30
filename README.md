# Customer Churn Prediction Using SVM

## 📌 Project Overview

Customer churn occurs when a customer stops using a company's products or services. 
Predicting customer churn can help businesses understand customer behavior and 
support customer retention strategies.

This project develops a **Customer Churn Prediction model using Support Vector Machine (SVM)** 
with the Telco Customer Churn dataset. The project includes data cleaning, exploratory 
data analysis, feature preprocessing, SVM model development, hyperparameter tuning, 
model evaluation, and a Streamlit web application for making predictions.

---

## 🎯 Project Objective

The main objective of this project is to develop a machine learning classification 
model that predicts whether a customer is likely to **churn or remain with the company**.

The project also focuses on:

- Cleaning and preparing customer data
- Exploring patterns related to customer churn
- Applying appropriate preprocessing techniques
- Comparing different SVM kernels
- Optimizing SVM hyperparameters using GridSearchCV
- Evaluating the model using multiple classification metrics
- Deploying the trained model through a Streamlit application

---

## 📊 Dataset

The project uses the **Telco Customer Churn dataset**, which contains information 
about customer demographics, subscribed services, contract details, and billing information.

### Dataset Size

- **Records:** 7,043 customers
- **Features:** 21 columns
- **Target Variable:** `Churn`

### Target Distribution

| Churn Status | Number of Customers | Percentage |
|--------------|--------------------:|-----------:|
| No           | 5,174               | 73.46%     |
| Yes          | 1,869               | 26.54%     |

The target variable is somewhat imbalanced, with non-churned customers representing 
the majority class.

---

## 🧹 Data Preprocessing

The following preprocessing steps were performed:

- Checked the dataset shape and data types
- Checked for duplicate records
- Identified missing values
- Handled missing values in `TotalCharges`
- Separated numerical and categorical features
- Encoded the target variable
- Applied one-hot encoding to categorical features
- Applied standard scaling to numerical features
- Used `ColumnTransformer` to apply different preprocessing techniques to different feature types
- Used a `Pipeline` to combine preprocessing and the SVM model

### Missing Value Handling

The `TotalCharges` column initially contained 11 missing values. 
These records had a tenure of 0 months, so the missing values were replaced with 0.

---

## 🔍 Exploratory Data Analysis

Several analyses were performed to understand customer churn patterns.

### Categorical Analysis

- Churn distribution
- Churn by contract type
- Churn by internet service
- Churn by payment method

### Numerical Analysis

- Tenure vs Churn
- Monthly Charges vs Churn
- Total Charges vs Churn

### Key Observations

- Month-to-month contract customers account for a large number of churned customers.
- Fiber optic customers show a high number of churned customers.
- Electronic check is associated with a high number of churned customers.
- Churned customers generally have shorter tenure.
- Churned customers generally show higher monthly charges.
- Non-churned customers generally have higher total charges, which may be related to their longer tenure.

These observations were used to guide the model preprocessing and development stages.

---

## 🤖 Machine Learning Model

### Support Vector Machine (SVM)

Support Vector Machine was selected as the classification algorithm for predicting 
customer churn.

The model uses:

- Numerical feature scaling using `StandardScaler`
- Categorical feature encoding using `OneHotEncoder`
- `ColumnTransformer` for combined preprocessing
- `Pipeline` for preprocessing and model integration
- `SVC` as the classification algorithm

---

## 🔬 SVM Kernel Comparison

Three SVM kernels were evaluated:

| Kernel | Accuracy | Precision | Recall | F1 Score |
|--------|---------:|----------:|-------:|---------:|
| Linear | 78.78% | 61.76% | 52.67% | 56.85% |
| RBF | 79.13% | 64.18% | 48.40% | 55.18% |
| Polynomial | 78.85% | 63.01% | 49.20% | 55.26% |

The three kernels showed relatively similar performance, so hyperparameter 
optimization was performed using GridSearchCV.

---

## ⚙️ Hyperparameter Optimization

`GridSearchCV` with **5-fold cross-validation** was used to optimize the SVM model.

The parameters explored included:

- `C`
- `kernel`
- `gamma`

The model was optimized using **F1-score** as the scoring metric because the 
target variable is somewhat imbalanced.

### Best Parameters

```text
C = 0.1
Kernel = Linear
Gamma = scale


### Best Cross-Validation F1 Score

**58.79%**

---

## 📈 Model Evaluation

The tuned SVM model was evaluated on the test dataset.

| Metric | Score |
|--------|------:|
| Accuracy | 78.92% |
| Precision | 62.07% |
| Recall | 52.94% |
| F1 Score | 57.14% |
| ROC-AUC | 82.72% |

The tuned SVM achieved a **ROC-AUC score of 82.72%**, indicating good ability to
distinguish between customers who churn and customers who do not churn based on
the model's decision scores.

---


## 🌐 Streamlit Application

The project includes an interactive Streamlit application as well.
