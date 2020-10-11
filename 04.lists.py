lesson_dates = [
    '14.09.2020',
    '19.09.2020',
    '21.09.2020',
    '27.09.2020',
    '28.09.2020'
 ]
student_marks = [5, 4, 3, 2, 5]

# i = 0
# while i < len(student_marks):
#     print(lesson_dates[i], 'оценка', student_marks[i])
#     i += 1

# for item in student_marks:  # item
#     print('оценка', item)
#
# for item in enumerate(student_marks):  # pairs -> (num, item)
#     print('оценка', item)

for item in enumerate(student_marks):  # pairs -> (num, item)
    i, mark = item
    print('оценка', item, 'или', i, mark)


# for item in enumerate(student_marks):  # pairs -> (num, item)
#     print('оценка', item)


# feature
# in place
for i, mark in enumerate(student_marks):  # pairs -> (num, item)
    print('оценка', i, mark)
    # print(lesson_dates[i], 'оценка', mark)
