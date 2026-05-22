num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

square = [i ** 2 for i in num]

print(square)

num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

even = [i for i in num1 if i % 2 == 0]
print(f"Evcen Number Only: {even}")

chr = ["hello", "WORLD", "PyThOn"]
e = [i.lower() for i in chr]
print(e)
