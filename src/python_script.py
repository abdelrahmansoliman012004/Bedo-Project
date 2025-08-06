import os
import pandas as pd  # pyright: ignore[reportMissingModuleSource]
from xgboost import XGBClassifier  # type: ignore
from sklearn.model_selection import train_test_split  # type: ignore
from sklearn.metrics import classification_report, accuracy_score  # type: ignore
import numpy as np
import joblib  # type: ignore
from datetime import datetime

# Load data
df = pd.read_csv(r"D:\Bedo project\student_dataset.csv")

# Drop unnecessary columns
df.drop(columns=[
    "Phone_No.", "Roll No.", "School Name", "Student Address", "Comment", "Student_Names"
], inplace=True)

# Encode grades to numeric
grade_mapping = {
    'A+': 0, 'A': 1, 'B+': 2, 'B': 3, 'C': 4, 'D': 5, 'F': 6
}
df['Grade'] = df['Grade'].map(grade_mapping)

# Split features and target
X = df.drop(columns=["Grade"])
y = df["Grade"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train model
model = XGBClassifier(
    n_estimators=100,
    max_depth=6,
    learning_rate=0.1,
    objective='multi:softmax',
    num_class=7,
    eval_metric='mlogloss'
)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report_dict = classification_report(y_test, y_pred, output_dict=True)
report_df = pd.DataFrame(report_dict).transpose()
report_df.loc['accuracy'] = [accuracy, np.nan, np.nan, np.nan]

# Save with timestamped filename
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_path = fr"D:\Bedo project\results_{timestamp}.csv"
report_df.to_csv(output_path, index=True)
print(f"\nResults saved to: {output_path}")

# Save model
model_path = r"D:\Bedo project\xgb_model.pkl"
joblib.dump(model, model_path)
print(f"Model saved to: {model_path}")
