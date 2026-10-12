
import numpy as np
student_scores = np.array([
    [85, 90, 78, 88],
    [92, 85, 80, 75],
    [78, 88, 92, 84],
    [90, 95, 85, 91]
])
average_scores = np.mean(student_scores, axis=0)
subjects = ["Math", "Science", "English", "History"]
print("Average marks for each subject:")
for i in range(len(subjects)):
    print(subjects[i], ":", average_scores[i])
highest_index = np.argmax(average_scores)

print("\nSubject with the highest average:",
      subjects[highest_index])
print("Highest average marks:", average_scores[highest_index])

