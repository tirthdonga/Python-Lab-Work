for i in range(1, 51, 1):
  if i % 2 == 0 and i % 3 == 0:
    print(i, "divisible by both")
  elif i % 2 ==  0:
    print(i, "divisible by 2")
  elif i % 3 == 0:
    print(i, "divisible by 3")