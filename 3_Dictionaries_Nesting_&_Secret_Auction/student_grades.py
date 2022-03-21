student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

# This is the scoring criteria:
# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"

#TODO-1: Create an empty dictionary called student_grades.

# student_grades = {}
#TODO-2: Write your code below to add the grades to student_grades.👇
# version 1
# student_grades = dict(student_scores) # copying student_scores to the student_grades

# for name, score in student_grades.items(): #loping through student_grades score and names
#   if score <= 70: # if score of the student is less than or equal to 70
#     student_grades[name] = "Fail" # change the score to mark "Fail"
#   if score >= 71 and score <= 80:
#     student_grades[name] = "Acceptable"
#   if score >= 81 and score <= 90:
#     student_grades[name] = "Exceeds Expectations"
#   if score >= 91 and score <= 100:
#     student_grades[name] = "Outstanding"

# version 2

# for student in student_scores:
#   score = student_scores[student]
#   if score > 90:
#     student_grades[student] = "Outstanding"
#   elif score > 80:
#     student_grades[student] = "Exceeds Expectations"
#   elif score > 70:
#     student_grades[student] = "Acceptable"
#   else:
#     student_grades[student] = "Fail"

# Expected Output
# '{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'
# 🚨 Don't change the code below 👇
# print(student_grades)