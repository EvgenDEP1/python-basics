lesson_dates = [
    '14.09.2020',
    '19.09.2020',
    '21.09.2020',
    '27.09.2020',
    '28.09.2020'
 ]
student_marks = [
    5,
    4,
    3,
    2,
    5
]
student_2_marks = [
    4,
    3,
    5,
    5,
    4
]

# lesson_dates_and_marks = [
#     ['14.09.2020', 5],
#     ['19.09.2020', 4],
#     ['21.09.2020', 3],
#     ['27.09.2020', 2],
#     ['28.09.2020', 5],
#  ]

# i = 0
# while i < len(student_marks):
#     print(lesson_dates[i], 'оценка', student_marks[i])
#     i += 1

# for item in student_marks:  # item
#     print('оценка', item)
#
# for item in enumerate(student_marks):  # pairs -> (num, item)
#     print('оценка', item)

# for item in enumerate(student_marks):  # pairs -> (num, item)
#     i, mark = item
#     print('оценка', item, 'или', i, mark)


# for item in enumerate(student_marks):  # pairs -> (num, item)
#     print('оценка', item)


# feature
# in place
# for i, mark in enumerate(student_marks):
#     print(lesson_dates[i], 'оценка', mark)


# Union
# for record in lesson_dates_and_marks:
#     lesson_date, mark = record
#     print(lesson_date, 'оценка', mark)
#     # print(record, 'или', lesson_date, mark)


# for lesson_date, mark in lesson_dates_and_marks:
#     print(lesson_date, 'оценка', mark)

# for lesson_date, mark in zip(lesson_dates, student_marks):
#     print(lesson_date, 'оценка', mark)


for lesson_date, mark, mark_2 in zip(lesson_dates, student_marks, student_2_marks):
    print(lesson_date, 'оценка', mark, mark_2)
