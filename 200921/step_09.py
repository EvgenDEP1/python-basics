class_pupils = 'полина ,антОн, арсений , евГений, алексей, тиМуР'
correct_result = ['Полина', 'Антон', 'Арсений', 'Евгений', 'Алексей', 'Тимур']

_result = class_pupils.split(',')
result = []
for item in _result:
    # result.append(item.strip())
    # result.append(item.strip().lower().title())
    result.append(item.strip().title())


assert result ==correct_result, 'алгоритм реализован неверно'
