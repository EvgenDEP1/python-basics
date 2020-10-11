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

print('Программа для вывода оценок по определёной дате.')

for lesson_date, mark, mark_2 in zip(lesson_dates, student_marks, student_2_marks):
    print('Дата:', lesson_date, 'Оценки за эту дату:', mark, mark_2)

# date = input('Введите дату:\n')
# a = lesson_dates.index(date)
# print('Оценка', student_marks[a], 'и', student_2_marks[a], 'за дату', date)

while True:
    date = input('Введите дату:\n')
    if date:
        if lesson_dates.count(date):
            a = lesson_dates.index(date)
            print('Оценка', student_marks[a], 'и', student_2_marks[a], 'за дату', date)
        else:
            print('такой даты нет')
    else:
        break

