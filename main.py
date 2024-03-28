import numpy as np
from cda import table


# This function helps us find student with the most points
def highest_average(x):
    numeric_matrix = x[1:, 1:].astype(int)
    average_points = np.mean(numeric_matrix, axis=1)
    max_index = np.argmax(average_points)
    student_name = x[max_index + 1, 0]
    student_average_points = average_points[max_index]
    return student_name, student_average_points


# To find out student with the lowest points in subject, we set 0 as definer, in opposite case, to find out highest
# points, we set definer as 1
def highest_or_lowest_points(x, subject, definer=0):
    subject_index = np.where(x[0] == subject)[0][0]
    numeric_points = x[1:, subject_index].astype(int)
    if definer == 0:
        min_score_index = np.argmin(numeric_points)
        min_score_student = x[min_score_index + 1, 0]
        return min_score_student, min_score_index
    elif definer == 1:
        max_score_index = np.argmax(numeric_points)
        max_score_student = x[max_score_index + 1, 0]
        return max_score_student, max_score_index


# This function takes table and name of subjects as parameter and returns all students, whose points are above average
def above_average_points(x, subject):
    subject_index = np.where(x[0] == subject)[0][0]
    numeric_points = x[1:, subject_index].astype(int)
    average_points = np.mean(numeric_points)
    print(f'Average points for {subject} is: {average_points} points\nList of students, with points above average:')
    result = ()
    for row in x[1:]:
        student = row[0]
        point = int(row[2])
        if point > average_points:
            result += (student, point)
    return np.array(result)

