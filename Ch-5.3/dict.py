student = {'name' : "Alice", 'age' : 20, 'grade' : "A"}

print(f"Key: {list(student.keys())}")
print(f"Value: {list(student.values())}")

student['city'] = "Delhi"

student['age'] = 21

student.pop('grade')
print(student)