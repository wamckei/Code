# Read from one dict, compare values and assign new values based on "Scores" to a new dict. 
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for x in student_scores:
    if student_scores[x] >= 91:
        student_grades[x] = "Outstanding"
    elif student_scores[x] >= 81 and student_scores[x] <= 90:
        student_grades[x] = "Exceeds Expectations"
    elif student_scores[x] >= 71 and student_scores[x] <= 80:
        student_grades[x] = "Acceptable"
    else:
        student_grades[x] = "Fail"

print(student_grades)

