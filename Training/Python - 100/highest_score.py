# Student score list
student_scores = [128, 143, 56, 78, 90, 210, 180, 156, 67, 82, 34, 65, 100, 101, 132, 77]

# Sums all items in the list
total_exam_score = sum(student_scores)
print(total_exam_score)

# Or to sum it manually use a loop
score = 0
for i in student_scores:
    score += i

print(score)

# Get the max item in the list
print(max(student_scores))

# Or manually determine the max with a loop
max_score = 0
for x in student_scores:
    if x > max_score:
        max_score = x

print(max_score)