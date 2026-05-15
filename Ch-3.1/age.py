age = int(input("Please Enter Your Age:- "))
'''
if age >= 0 and age <= 12:
  print("You are child")

elif age >= 13 and age <= 19:
  print("You are teenager")

elif age >= 20 and age <= 59:
  print("you are adult")

elif age >= 60:
  print("You are senior")

else:
  print("Stupid")
  '''
if age >= 12:
  if age >= 19:
    if age >= 59:
      print("you are Senior")
    else:
      print("you are Adult")
  else:
    print("you are teenager")
else:
  print("You are child")
