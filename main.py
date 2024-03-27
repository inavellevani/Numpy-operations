import numpy as np

# table elements
georgian_first_names = np.array(['ვენერა', 'თინა', 'თეა', 'სოსო', 'მირანდა', 'ჟენია', 'ტატიანა', 'ედუარდ',
                                 'კლარა', 'სიმონ', 'ანზორ', 'სოფია', 'სოსო', 'ნელი', 'ბონდო', 'ედუარდ',
                                 'სონია', 'არჩილ', 'მარიამ', 'სოფია', 'ემა', 'იზოლდა', 'ომარ', 'ტატიანა',
                                 'ვიქტორ', 'კარინე', 'გუგული', 'კახა', 'როზა', 'რუსუდან', 'სიმონ', 'ნელი',
                                 'ბადრი', 'მადონა', 'ირინე', 'მინდია', 'ნათია', 'გულნარა', 'კახა', 'ელზა',
                                 'როინ', 'ნაირა', 'ლიანა', 'ნინელი', 'მაყვალა', 'რეზო', 'ჟუჟუნა', 'ზინა',
                                 'გოჩა', 'მურმან'])

georgian_last_names = np.array(
    ['ქუთათელაძე', 'მეგრელიშვილი', 'სალუქვაძე', 'ხარაიშვილი', 'შელია', 'კევლიშვილი',
     'ბუჩუკური', 'ტყებუჩავა', 'მიქაბერიძე', 'ურუშაძე', 'ძიძიგური', 'გოგუაძე', 'ანთაძე',
     'ვალიევა', 'როგავა', 'ნაკაშიძე', 'ღურწკაია', 'გვაზავა', 'გვასალია', 'ზარანდია',
     'სხირტლაძე', 'ბერაძე', 'ხვიჩია', 'ბასილაშვილი', 'კაკაბაძე', 'მერებაშვილი', 'ნოზაძე',
     'ხარაბაძე', 'მუსაევა', 'მამულაშვილი', 'ელიზბარაშვილი', 'მამულაშვილი', 'ჯოჯუა',
     'გულუა', 'ხალვაში', 'ხარატიშვილი', 'დუმბაძე', 'ბერიანიძე', 'ჯოხაძე', 'სამხარაძე',
     'ლიპარტელიანი', 'იობიძე', 'გაბაიძე', 'ხარაბაძე', 'ინასარიძე', 'ბერაძე', 'შენგელია',
     'ქობალია', 'მიქავა', 'რევაზიშვილი'])

subjects = np.array(['მათემატიკა', 'ინგლისური', 'ალგორითები', 'CCNA შესავალი', 'Frontend'])

num_students = 100
num_subjects = len(subjects)

# generating table elements
random_first_names = np.random.choice(georgian_first_names, size=num_students)
random_last_names = np.random.choice(georgian_last_names, size=num_students)
random_full_names = np.array([f'{first} {last}' for first, last in zip(random_first_names, random_last_names)])
points = np.random.randint(0, 101, size=(num_students, num_subjects))

# Table design
table = np.column_stack((random_full_names, points))
table = np.vstack((np.concatenate((['სტუდენტი'], subjects)), table))
# print(table)
# print('\n')

# Student with the highest average points
numeric_matrix = table[1:, 1:].astype(int)
average_points = np.mean(numeric_matrix, axis=1)
max_index = np.argmax(average_points)
student_name = table[max_index + 1, 0]
student_average_points = average_points[max_index]
# print(f'Student with highest average points:\n{student_name} : {student_average_points}')
# print('\n')

# Highest and lowest points in maths
subject_index = np.where(table[0] == 'მათემატიკა')[0][0]
numeric_points = table[1:, subject_index].astype(int)
max_score_index = np.argmax(numeric_points)
min_score_index = np.argmin(numeric_points)
max_score_student = table[max_score_index + 1, 0]
min_score_student = table[min_score_index + 1, 0]
# print(f'Student with the highest points in მათემატიკა: {max_score_student} - {numeric_points[max_score_index]} points')
# print(f'Student with the lowest points in მათემატიკა: {min_score_student} - {numeric_points[min_score_index]} points')
# print('\n')

# Students with higher points, than English average points
subject_index = np.where(table[0] == 'ინგლისური')[0][0]
numeric_points = table[1:, subject_index].astype(int)
average_english = np.mean(numeric_points)

# print(f'Average points in English: {average_english}')
# print(f'List of students, with points above average:')
# for row in table[1:]:
#     student = row[0]
#     points = int(row[2])
#     if points > average_english:
#         print(f'{student}: {points}')
