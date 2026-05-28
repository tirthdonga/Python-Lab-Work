def factorial():
  a = int(input("Enter The Number You Want Factorial Of: "))
  s = 1
  for a in range(1, a + 1):
    s *= a
  print(f"Factorial Of {a} is: {s}")

factorial()