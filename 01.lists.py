student_marks = []
while True:
    mark = input('Введите оценку студента:\n')
    if mark:
        student_marks.append(mark)
    else:
        break
print('Ввод завершен')
print(student_marks)