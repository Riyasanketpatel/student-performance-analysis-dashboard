import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# ================== CREATE FOLDER ==================
os.makedirs("static/plots", exist_ok=True)

# ================== SAVE FUNCTION ==================
def save_plot(name):
    plt.tight_layout()
    plt.savefig(f"static/plots/{name}.png", dpi=300, bbox_inches="tight")
    plt.close()

# ================== LOAD DATA ==================
df = pd.read_csv("clean_enhanced_student_data.csv")

# # ================== NEW FEATURE ==================
# df["entertainment_hours"] = df["social_media_hours"] + df["netflix_hours"]
# # ================== REGPLOTS ==================
# plt.figure(figsize=(8,5))
# sns.regplot(data=df, x="previous_gpa", y="exam_score", line_kws={"color": "green"})
# plt.title("Impact of Previous GPA on Exam Score")
# save_plot("gpa_vs_score")

# plt.figure(figsize=(8,5))
# sns.regplot(data=df, x="study_hours_per_day", y="exam_score", line_kws={"color": "purple"})
# plt.title("Daily Study Hours effecting Exam Score")
# save_plot("study_vs_score")

# sns.regplot(data=df, x="attendance_percentage", y="exam_score",line_kws={"color":"red"})
# plt.title("Attendance vs Exam Score")
# save_plot("Attendance_vs_score")

# plt.figure(figsize=(8,5))
# sns.regplot(data=df, x="motivation_level", y="exam_score",
#             scatter_kws={"alpha":0.3}, line_kws={"color":"red"})
# plt.title("Motivation Level vs Exam Score")
# save_plot("motivation_vs_score")

# plt.figure(figsize=(8,5))
# sns.regplot(data=df, x="exam_anxiety_score", y="exam_score", line_kws={"color": "red"})
# plt.title("Exam Anxiety vs Exam Score")
# save_plot("anxiety_vs_score")

# plt.figure(figsize=(7,5))
# sns.regplot(data=df,x="stress_level",y="exam_score",line_kws={"color": "red"})
# plt.title("Stress Level vs Exam Score")
# save_plot("stress_vs_score")


# plt.figure(figsize=(8,5))
# sns.regplot(x="entertainment_hours", y="exam_score", data=df, scatter=False)
# plt.title("Effect of Entertainment Hours on Exam Score")
# save_plot("entertainment_vs_score")

# plt.figure(figsize=(8,5))
# sns.regplot(data=df, x="screen_time", y="exam_score", line_kws={"color": "orange"})
# plt.title("Screen Time vs Exam Score")
# save_plot("screentime_vs_score")

# sns.histplot(df["exam_score"], kde=True)
# plt.title("Exam Score Distribution")
# save_plot("sore_distribution")

# # ================== TOPPER ANALYSIS ==================
# df_top = df.sort_values(by="exam_score", ascending=False).head(10).copy()
# df_top["Rank"] = range(1, len(df_top) + 1)

# df_melted = df_top.melt(
#     id_vars="student_id",
#     value_vars=["study_hours_per_day", "entertainment_hours"],
#     var_name="Activity",
#     value_name="Hours"
# )

# plt.figure(figsize=(12,6))
# sns.barplot(data=df_melted, x="student_id", y="Hours", hue="Activity")
# plt.title("Study vs Entertainment Hours for Top Scorers")
# plt.xlabel("Top 10 Students")
# plt.ylabel("Hours")
# plt.xticks(rotation=45)
# save_plot("topper_study_vs_entertainment")

# # ================== MAJOR VS ENVIRONMENT ==================
# major_env = pd.pivot_table(
#     df,
#     values="exam_score",
#     index="major",
#     columns="study_environment",
#     aggfunc="mean"
# )

# plt.figure(figsize=(12,6))
# sns.heatmap(major_env, annot=True, fmt=".1f", cmap="YlOrRd", linewidths=0.5)
# plt.title("Major student preferring Study Environment")
# save_plot("major_vs_study_environment")

# print("✅ All plots saved successfully in static/plots/")


model_results = pd.DataFrame({

    "Model": ["Linear Regression", "Ridge", "Lasso", "Random Forest"],

    "R2": [
        0.8703789351001365,
        0.8703788557159973,
        0.8703546302020162,
        0.8682897710464398
    ],

    "Adjusted R2": [
        0.8700051766230229,
        0.8700132451172271,
        0.8699889512725372,
        0.8679182679561233
    ],

    "MAE": [
        3.1968,
        3.1968,
        3.2078,
        3.3072
    ],

    "RMSE": [
        4.1891,
        4.1891,
        4.1895,
        4.2227
    ],

    "MAPE": [
        0.03803,
        0.03803,
        0.03818,
        0.03918
    ]

})
plt.figure(figsize=(10,6))
model_results.set_index("Model")[["R2", "MAE", "RMSE"]].plot(kind="bar")
plt.title("Model Performance Comparison")
plt.ylabel("Score")
plt.xticks(rotation=45)
plt.tight_layout()
save_plot("model_comparison.png")

print("✅ Model comparison graph saved!")