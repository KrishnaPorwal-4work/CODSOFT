# 🚢 Titanic Survival Prediction App

## 📌 Overview

This project aims to predict whether a passenger survived the Titanic disaster using Machine Learning. It is a binary classification problem where the target variable indicates survival (1) or not (0).

The model is trained on passenger data including demographic and travel details, and provides predictions based on user input.

---

## 🚀 Features

* 📊 Performed Exploratory Data Analysis (EDA) using visualizations
* 🧹 Data cleaning and handling missing values
* 🧠 Feature engineering:

  * Created **FamilySize** feature
  * Created **IsAlone** indicator
* 🤖 Built classification model using Logistic Regression
* 📈 Model evaluation using:

  * Confusion Matrix
  * Precision, Recall, F1-score
* 🌐 Interactive prediction system (can be extended to Streamlit app)

---

## 🧠 Dataset

The dataset contains **891 passenger records** with the following key features:

* Pclass (Passenger Class)
* Sex
* Age
* SibSp (Siblings/Spouses aboard)
* Parch (Parents/Children aboard)
* Fare
* Embarked (Port of embarkation)
* Survived (Target Variable)

---

## ⚙️ Tech Stack

* **Programming Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-learn
* **Visualization:** Matplotlib, Seaborn

---

## 🧹 Data Preprocessing

* Dropped **Cabin** column due to high missing values (~77%)
* Filled missing values:

  * Age → Median
  * Embarked → Mode
* Encoded categorical variables:

  * Sex → Label Encoding
  * Embarked → One-Hot Encoding
* Removed unnecessary columns:

  * Name, Ticket, PassengerId

---

## 🧠 Feature Engineering

* **FamilySize = SibSp + Parch + 1**
* **IsAlone**:

  * 1 → Passenger is alone
  * 0 → Not alone

These features improved model performance and helped capture passenger context.

---

## 📊 Exploratory Data Analysis (EDA)

Key insights:

* Female passengers had higher survival rates
* Passengers in higher classes (Pclass 1) had better survival chances
* Age distribution showed most passengers were young adults

---

## 🤖 Model Building

* Split data into training (75%) and testing (25%)
* Used Logistic Regression for classification

---

## 📈 Model Performance

* Achieved **~80% accuracy** on test data

### 🔍 Confusion Matrix

* Correct Predictions: 179
* Incorrect Predictions: 44

### 📊 Classification Metrics

* Precision (Survived): ~0.77
* Recall (Survived): ~0.72
* F1-score: ~0.74

> ⚠️ Note: Model performs better for non-survivors due to class imbalance in the dataset.

---

## ▶️ How to Run Locally

### 1️⃣ Clone the repository

```id="rnhg9f"
git clone https://github.com/your-username/titanic-survival-prediction.git
```

### 2️⃣ Navigate to the project folder

```id="b7pl0v"
cd titanic-survival-prediction
```

### 3️⃣ Install dependencies

```id="n6r6xg"
pip install -r requirements.txt
```

### 4️⃣ Run the notebook / app

```id="yq3gk8"
jupyter notebook
```

---

## 💡 Future Improvements

* Apply advanced models (Random Forest, XGBoost)
* Handle class imbalance more effectively
* Perform hyperparameter tuning
* Deploy as a Streamlit web application

---

---

## 👨‍💻 Author

**Krishna Porwal**

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
