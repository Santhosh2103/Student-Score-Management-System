import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Grading function
def grade(score):
    if score >= 90:
        return 'A+'
    elif score >= 80:
        return 'A'
    elif score >= 70:
        return 'B'
    elif score >= 60:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'

st.title("🎓 Student Score Management System")

# File uploader
uploaded_file = st.file_uploader("📤 Upload CSV file with student scores", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("📊 Raw Data")
    st.dataframe(df)

    # Auto-select score columns (skip name/id)
    score_columns = df.columns[1:]
    st.write("✅ Score Columns being used:", score_columns.tolist())

    # Convert all selected score columns to numeric safely
    df[score_columns] = df[score_columns].apply(pd.to_numeric, errors='coerce')

    # Calculate results
    df['Total'] = df[score_columns].sum(axis=1, skipna=True)
    df['Average'] = df['Total'] / len(score_columns)
    df['Grade'] = df['Average'].apply(grade)

    # Show processed results
    st.subheader("✅ Processed Results with Grades")
    st.dataframe(df[['Total', 'Average', 'Grade']])

    # Bar chart of grade counts
    st.subheader("📈 Grade Distribution")
    grade_counts = df['Grade'].value_counts().sort_index()
    st.bar_chart(grade_counts)
