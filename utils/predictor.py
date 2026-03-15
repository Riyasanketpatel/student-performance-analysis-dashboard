import pandas as pd
import numpy as np
import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model = joblib.load(os.path.join(BASE_DIR, "model", "linear_regression.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "model", "scaler.pkl"))
columns = joblib.load(os.path.join(BASE_DIR, "model", "columns.pkl"))

def convert_cgpa(cgpa):
    if cgpa > 4:
        return (cgpa / 10) * 4
    return cgpa

def predict_student(data):

    data["previous_gpa"] = convert_cgpa(float(data["previous_gpa"]))

    df = pd.DataFrame([data])

    df = pd.get_dummies(df)
    df = df.reindex(columns=columns, fill_value=0)

    df = scaler.transform(df)

    prediction = model.predict(df)[0]

    return round(prediction, 2)