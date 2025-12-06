# 📱 Used Smartphone Price Predictor

This project predicts the **fair resale price** of used smartphones based on their technical specifications.  
The goal is to bring consistency and data-driven accuracy to the second-hand smartphone market, where pricing is often subjective and unreliable.

---

## 🔍 Problem Statement
Used smartphone prices vary widely across sellers and online platforms due to inconsistent evaluations, negotiation margins, and lack of standard pricing methods.

This project builds a machine learning model that predicts a **fair, transparent resale price** using key device features such as:
- Brand  
- RAM  
- Storage  
- Battery capacity  
- Processor score  
- Screen size  
- Release year  
- Physical condition  

---

## 🚀 What This Project Achieves
- Processes messy real-world price data  
- Performs complete Exploratory Data Analysis (EDA)  
- Implements **manual Gradient Descent** to learn Linear Regression  
- Trains a **scikit-learn Linear Regression model**  
- Evaluates model performance using MSE/RMSE  
- Builds a clean prediction function for new smartphone inputs  

This notebook demonstrates both **conceptual understanding** and **practical ML workflow**.

---

## 📂 Project Structure
```
📁 Used-Phone-Price-Predictor
│── ML_PROJECT_1.ipynb      # Full project notebook
│── model.pkl               # Trained sklearn model
│── README.md               # Project documentation
└── data.csv (optional)     # Dataset used for training
```

---

## 🧠 Workflow Summary

### 1️⃣ Data Cleaning
- Converted price strings (e.g., "₹12,999", "12k") into numeric values  
- Removed unnecessary columns  
- Handled missing values  
- Normalized price values  

### 2️⃣ Exploratory Data Analysis (EDA)
- Distribution plots of numeric features  
- Correlation analysis  
- Understanding brand and condition impact  
- Identifying price-driving features  

### 3️⃣ Feature Engineering
- Transforming categorical values (brand, condition)  
- Creating numeric mappings  
- Preparing features for regression models  

### 4️⃣ Manual Gradient Descent Implementation
- Implemented Linear Regression from scratch  
- Computed gradients, updated weights  
- Visualized training loss  
- Compared results with sklearn model  

### 5️⃣ Training the sklearn Linear Regression Model
- Trained with processed dataset  
- Compared predictions with manual model  
- Saved trained model as `model.pkl` for reuse  

### 6️⃣ Prediction Function
- Accepts new smartphone specs  
- Outputs estimated fair resale price  
- Handles all preprocessing internally  

---

## 📊 Key Insights
- Brand and condition strongly influence resale price  
- Release year and processor score are major price drivers  
- Battery capacity has less influence than expected  
- Apple devices retain value much better than most brands  
- Linear Regression performs well for structured resale data  

---

## 📈 Future Improvements
- Add advanced ML models (Random Forest, XGBoost, Ridge, Lasso)  
- Build a complete sklearn Pipeline for deployment  
- Expand datasets with camera, chipset, and refurbishing grade  
- Deploy as an API or interactive web app  
- Add real-time scraping for dynamic pricing  

---

## 🛠 Tech Stack
- Python  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- scikit-learn  
- Jupyter Notebook  

---

## 🎯 Summary
This project delivers a full end-to-end machine learning workflow:
- Data cleaning  
- EDA  
- Manual ML implementation  
- scikit-learn modeling  
- Prediction system  

It’s a strong **first ML project** demonstrating both understanding and real-world application.

---

If you find this project helpful, feel free to ⭐ the repository and share feedback!
