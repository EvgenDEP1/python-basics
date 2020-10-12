# class_pupils = input('Введите имена учеников через запятую:\n')

class_pupils = 'Полина , Антон, Арсений , Евгений, Алексей, Тимур'
correct_result = ['Полина', 'Антон', 'Арсений', 'Евгений', 'Алексей', 'Тимур']

# print('Ученики класса:', class_pupils)

_result = class_pupils.split(', ')
result = []
for item in _result:
    result.append(item.strip())

print(result)

assert result ==correct_result, 'алгоритм реализован неверно'
