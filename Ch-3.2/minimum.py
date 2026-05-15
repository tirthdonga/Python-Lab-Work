a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

if a == b and b == c:
  print("All the Number are same")
else:
  if a < b:
    if a < c:
      print("A is Smallest Number")
    else:
      print("C is Smallest Number")
  else:
    if b < c:
      print("B is Smallest Number")
    else:
      print("C is Smallest Number")