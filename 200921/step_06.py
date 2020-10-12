avg_mark = input('Введите средний бал студента\n')
# if avg_mark.isdigit():
#     avg_mark = float(avg_mark)
#     print('Ввод корректен', type(avg_mark), avg_mark)

try:
    avg_mark = float(avg_mark)
    print('Ввод корректен', type(avg_mark), avg_mark)
except ValueError as e:
    print('некорректное значение:', avg_mark)


