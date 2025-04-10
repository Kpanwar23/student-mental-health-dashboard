import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the dataset
df = pd.read_excel("Cleaned_Student_Mental_Health.xlsx")

# Step 2: Basic Overview
print("First few rows:")
print(df.head())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

# Step 3: Gender distribution
gender_counts = df['choose_your_gender'].value_counts()
print("\nGender distribution:")
print(gender_counts)

# Gender difference
female_count = gender_counts.get('female', 0)
male_count = gender_counts.get('male', 0)
gender_diff = abs(female_count - male_count)
print(f"\nDifference between females and males: {gender_diff} student(s)")

# Bar chart
gender_counts.plot(kind='bar', title='Gender Distribution')
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

# Step 4: Depression analysis
depression_counts = df['do_you_have_depression?'].value_counts()
total_students = len(df)
depressed_students = depression_counts.get('yes', 0)
depression_percentage = (depressed_students / total_students) * 100

print(f"\nStudents with Depression: {depressed_students} out of {total_students} ({depression_percentage:.1f}%)")

# Pie chart
depression_counts.plot(kind='pie', autopct='%1.1f%%', title='Do Students Have Depression?')
plt.ylabel("")
plt.show()

# Step 5: Help-seeking behavior
help_counts = df['did_you_seek_any_specialist_for_a_treatment?'].value_counts()
help_yes = help_counts.get('yes', 0)
help_no = help_counts.get('no', 0)
help_percentage = (help_yes / total_students) * 100
help_diff = abs(help_yes - help_no)

print(f"\nStudents who Sought Help: {help_yes} out of {total_students} ({help_percentage:.1f}%)")
print(f"Difference between those who sought help and those who didn't: {help_diff} student(s)")

# Bar chart
help_counts.plot(kind='bar', title='Did Students Seek Professional Help?')
plt.xlabel("Response")
plt.ylabel("Number of Students")
plt.show()

# Step 6: Depression vs Seeking Help
depressed_df = df[df['do_you_have_depression?'] == 'yes']
depressed_and_help = depressed_df['did_you_seek_any_specialist_for_a_treatment?'].value_counts().get('yes', 0)
depressed_total = len(depressed_df)
help_if_depressed_pct = (depressed_and_help / depressed_total) * 100 if depressed_total > 0 else 0

print(f"\nAmong students with depression:")
print(f"- {depressed_total} students reported depression")
print(f"- {depressed_and_help} of them sought professional help")
print(f"- That’s {help_if_depressed_pct:.1f}% of depressed students seeking help")

print("\n✅ EDA Complete!")
