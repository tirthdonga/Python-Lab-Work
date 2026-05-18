stop = int(input("Enter number: "))
print("Printing the numbers that are divisible by 3 and 5")
for i in range(1, stop, 1):
  if i % 3 == 0 or i % 5 == 0:
    print(i, end=(" "))
