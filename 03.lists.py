mock_student_marks = [5, 4, 3, 2, 5]
# print(dir(mock_student_marks))

print(mock_student_marks)
mock_student_marks.append(5)
print(mock_student_marks)
# print(mock_student_marks.index(5))
# print(mock_student_marks.index(5, 1))
# print(mock_student_marks.index(5, 1, 5))

# print(mock_student_marks.count(5))
# print(mock_student_marks.count(2))

num = 4 # abstraction concrete number > variable num
if mock_student_marks.count(num):
    print(num, 'found', mock_student_marks.count(num), 'times, first index:', mock_student_marks.index(num))
else:
    print(num, 'not found')

