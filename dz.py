student_marks = []
while True:
    mark = input('Введите оценку студента:\n')
    if mark:
        if 1 <= int(mark) <= 5:
            student_marks.append(int(mark))
        else:
            print('оценка должна быть от 1 до 5')
    else:
        break
print('Ввод завершен')
print(student_marks)

avg_mark = 0
for item in student_marks:
    avg_mark += item

avg_mark /= len(student_marks)
print('Средний балл', avg_mark)

