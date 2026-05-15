a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
d = int(input("Enter a number: "))

if a == b and b == c and c == d:
  print("All the Number are same")
else:
  if a > b:
    if a > c:
      if a > d:
        print("A is Largest")
      else:
        print("D is Largest")
    else:   
      if c > d:
        print("C is Largest")
      else:
        print("D is Largest")
  else:
    if b > c:
      if b > d:
        print("B is Largest")
      else:
        print("D is Largest")
    else:   
      if c > d:
        print("C is Largest")
      else:
        print("D is Largest") 