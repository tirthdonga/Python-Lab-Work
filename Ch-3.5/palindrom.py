word = str(input("Enter Your String: "))

reversed_string = word[::-1]
if word.lower() == reversed_string.lower():
  print("Your Entered String is Palindrom string")
else:
  print("Your Entered String is not Palindrom String")

'''
Output:
Enter Your String: wow
Your Entered String is Palindrom string
'''