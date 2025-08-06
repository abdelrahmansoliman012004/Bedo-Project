# 🎓 Bedo Project – Student Grade Prediction using XGBoost

This repository is part of our internship at **Bedo Innovating Education**.  
Developed by **Abdelrahman Mohamed Mahmoud** and **Nour Mohamed** under the guidance of **Eng. Zainab**.

---

## 🧠 Project Summary

This project is a multi-class classification system to predict university student final grades (`A+`, `A`, `B+`, `B`, `C`, `D`, `F`) based on academic and behavioral indicators such as attendance, participation, and assessments.

---

## 📌 Objective

Help identify students at academic risk early by predicting final grades using machine learning.  
This can assist educators in planning timely interventions and support strategies.

---

## 📂 Project Structure

├── data/ # Contains the dataset (student_dataset.csv)
├── models/ # Saved trained models (e.g., xgb_model.pkl)
├── results/ # Evaluation reports with timestamps
├── src/ # Python source files (e.g., train_model.py)
├── README.md # This file
├── requirements.txt# Required Python packages
└── .gitignore # Files/folders to be ignored by Git

## 🚀 How to Run the Project

1. **Clone the repo:**
   ```bash
   git clone https://github.com/your-username/Bedo-Student-Grade-Prediction.git
   cd Bedo-Student-Grade-Prediction

2. **Install dependencies:**
   ```bash
    pip install -r requirements.txt
    
3. **Run the training script:**

   ```bash
    python src/train_model.py

**Outputs:**

Evaluation reports saved in: results/

Trained model saved in: models/

**📈 Evaluation Metrics**
Accuracy

Precision, Recall, F1-score (per class)

CSV classification report saved with timestamp for traceability

🙌 Acknowledgments
Special thanks to Eng. Zainab and the Bedo Innovating Education team for support and guidance.