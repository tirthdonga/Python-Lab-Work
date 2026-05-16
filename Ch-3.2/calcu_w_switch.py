a = int(input("Enter a Number: "))
b = int(input("Enter a Number: "))

operator = input("Enter a operator (+, -, *, /, %): ")

match operator:
  case "+" :
    print("a + b:", a + b)                                                                       
  case "-":
    print("a - b:", a - b)                                                                       
  case "*":
    print("a * b:", a * b)                                                                       
  case "/":
    print("a / b:", a / b)                                                                       
  case "%":
    print("a Modulace b:", a % b)                                                                       
  case _:
    print("unknow status")                                                                       