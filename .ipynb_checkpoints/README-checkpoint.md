# Customer Churn Prediction using Machine Learning

## Project Overview
This project focuses on predicting customer churn using machine learning techniques. The goal is to identify customers who are likely to leave a service so that businesses can take proactive steps to retain them.

---

## Objective
To build a predictive model that accurately identifies customers at risk of churn and provides actionable insights to improve customer retention.

---

## Dataset
The dataset contains customer usage details such as:
- Call minutes (day, evening, night, international)
- Customer service calls
- Account information
- Usage patterns

---

## Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn

---

## ⚙️ Approach

### 1. Data Preprocessing
- Handled missing values
- Converted categorical variables to numerical
- Feature scaling (for Logistic Regression)

### 2. Feature Engineering
- Total usage minutes
- Call ratios and patterns
- Complaint indicators

### 3. Model Building
- Logistic Regression
- Random Forest Classifier

### 4. Model Evaluation
- Accuracy
- Precision, Recall, F1-score
- Confusion Matrix

---

## Results

| Model                | Accuracy | Recall (Churn) |
|---------------------|----------|----------------|
| Logistic Regression | ~91%     | ~64%           |
| Random Forest       | **97%**  | **73**       |

---

## Key Insights
- High customer service calls strongly indicate churn
- Total usage and day-time usage significantly impact churn
- Complaint-related features increase churn probability

---

## Final Model
Random Forest Classifier (tuned)

- Accuracy: **97%**
- Recall: **100% (No churn customers missed)**

---

##  Business Impact
This model helps businesses:
- Identify at-risk customers
- Reduce churn rate
- Improve customer retention strategies

---

## Future Improvements
- Deploy model using Streamlit
- Hyperparameter tuning using GridSearchCV
- Handle class imbalance using advanced techniques (SMOTE)
