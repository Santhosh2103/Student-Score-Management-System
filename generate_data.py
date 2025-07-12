import pandas as pd
import random

names = [
    "Alice", "Bob", "Charlie", "David", "Eve", "Fay", "Grace", "Heidi",
    "Ivan", "Judy", "Karl", "Leo", "Mallory", "Niaj", "Olivia", "Peggy",
    "Quinn", "Rupert", "Sybil", "Trent"
]

data = []

for i, name in enumerate(names, start=1):
    math = random.randint(50, 100)
    science = random.randint(50, 100)
    english = random.randint(50, 100)
    attendance = random.randint(70, 100)
    
    data.append([i, name, math, science, english, attendance])

df = pd.DataFrame(data, columns=["StudentID", "Name", "Math", "Science", "English", "Attendance (%)"])

# Save to CSV
df.to_csv("data/student_scores.csv", index=False)
print("✅ Data generated and saved to student_scores.csv")