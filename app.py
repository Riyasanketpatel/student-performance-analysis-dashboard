from flask import Flask, render_template, request, redirect, url_for
from utils.predictor import predict_student
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("clean_enhanced_student_data.csv")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/visualization")
def visualization():

    total_students = len(df)
    avg_score = round(df["exam_score"].mean(),2)
    avg_study = round(df["study_hours_per_day"].mean(),2)
    avg_attendance = round(df["attendance_percentage"].mean(),2)

    return render_template(
        "visualization.html",
        total_students=total_students,
        avg_score=avg_score,
        avg_study=avg_study,
        avg_attendance=avg_attendance
    )

@app.route("/model-comparison")
def model_comparison():
    return render_template("model_comparison.html")

@app.route("/prediction", methods=["GET", "POST"])
def prediction():

    if request.method == "POST":

        data = {
            "study_hours_per_day": float(request.form["study_hours"]),
            "social_media_hours": float(request.form["social_media"]),
            "netflix_hours": float(request.form["netflix"]),
            "attendance_percentage": float(request.form["attendance"]),
            "sleep_hours": float(request.form["sleep"]),
            "previous_gpa": float(request.form["gpa"]),
            "stress_level": float(request.form["stress"]),
            "motivation_level": float(request.form["motivation"]),
            "screen_time": float(request.form["screen_time"]),
            "major": request.form["major"],
            "gender": request.form["gender"]
        }

        result = predict_student(data)

        return redirect(url_for("result", score=result))

    return render_template("prediction.html")

@app.route("/result")
def result():

    score = float(request.args.get("score"))

    if score >= 90:
        label = "Outstanding"
        color = "#28a745"
        message = "Exceptional performance! Keep aiming high."
    elif score >= 75:
        label = "Good"
        color = "#17a2b8"
        message = "You are doing great. A little more effort can make it outstanding."
    elif score >= 60:
        label = "Average"
        color = "#ffc107"
        message = "Decent performance. Focus more on study consistency."
    else:
        label = "Needs Improvement"
        color = "#dc3545"
        message = "You need a structured study plan and better habits."

    return render_template(
        "result.html",
        score=score,
        label=label,
        color=color,
        message=message
    )
    
if __name__ == "__main__":
    app.run(debug=True)