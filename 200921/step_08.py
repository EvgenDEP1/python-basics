class_pupils = 'Полина ,Антон, Арсений , Евгений, Алексей, Тимур'
correct_result = ['Полина', 'Антон', 'Арсений', 'Евгений', 'Алексей', 'Тимур']

# _result = class_pupils.split(',')
# result = []
# for item in _result:
#     result.append(item.strip())

# result = list(map(str.strip, class_pupils.split(',')))
result = [item.strip() for item in class_pupils.split(',')]

assert result ==correct_result, 'алгоритм реализован неверно'
