# 📊 Sales Prediction using Machine Learning

## 🚀 Overview
This project uses machine learning to predict product sales based on advertising spend across different channels like TV, Radio, and Newspaper.

---

## 🎯 Problem Statement
The goal is to build a regression model that can estimate sales based on marketing budgets, helping businesses optimize advertising strategies.

---

## 📂 Dataset
The dataset contains 200 records with the following features:

- TV Advertising Spend
- Radio Advertising Spend
- Newspaper Advertising Spend
- Sales (Target Variable)

---

## 🔍 Exploratory Data Analysis
- TV and Radio have strong positive correlation with Sales
- Newspaper has very weak correlation
- Dataset is clean with no missing values

---

## 🧠 Feature Selection
Newspaper feature was removed and the model performance remained unchanged, indicating it has minimal impact on sales.

---

## 🤖 Model Used
- Linear Regression

---

## 📈 Model Performance
- R² Score: ~0.88
- MAE: ~1.29
- MSE: ~3.00

---

## 📊 Visualizations
- Actual vs Predicted Plot
- Feature Importance Graph

---

## 💡 Key Insights
- TV advertising contributes the most to sales
- Radio advertising has strong per-unit impact
- Newspaper advertising has negligible influence

---

## ⚙️ Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## 🚀 Future Improvements
- Try advanced models (Random Forest, XGBoost)
- Deploy using Streamlit
- Hyperparameter tuning

---

## 📌 Conclusion
The model successfully predicts sales with good accuracy and provides actionable insights into advertising effectiveness.

---

## 👨‍💻 Author
Krishna Porwal