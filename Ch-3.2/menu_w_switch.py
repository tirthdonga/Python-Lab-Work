print("- Press 1 to order Sandwich")
print("- Press 2 to order Burger")
print("- Press 3 to order Pizza")

press = int(input("\nEnter the number: "))

match press:

  case 1:
    print("\n-----Sandwich Menu-----")
    print("\n- Press 1 to order Chesse Sandwich")
    print("- Press 2 to order Grilled Sandwich")
    print("- Press 3 to order Salad Sandwich")
    press1 = int(input("\nEnter the number: "))

    match press1:
      case 1:
        print("\nYou ordered Chesse Sandwich")
      case 1:
        print("\nYou ordered Grilled Sandwich")
      case 3:
        print("\nYou ordered Salad Sandwich")
      case _:
        print("\nWrong number entered")

  case 2:
    print("\n-----Burger Menu-----")
    print("\n- Press 1 to order Chesse Burger")
    print("- Press 2 to order Peri Peri Burger")
    print("- Press 3 to order Swazvan Burger")
    press1 = int(input("\nEnter the number: "))

    match press1:
      case 1:
        print("\nYou ordered Chesse Burger")
      case 2:
        print("\nYou ordered Peri Peri Burger")
      case 3:
        print("\nYou ordered Swazvan Burger")
      case _:
        print("\nWrong number entered")

  case 3:
    print("\n-----Pizza Menu-----")
    print("\n- Press 1 to order Chesse Pizza")
    print("- Press 2 to order Curst Pizza")
    print("- Press 3 to order Dough Pizza")
    press1 = int(input("\nEnter the number: "))

    match press1:
      case 1:
        print("\nYou ordered Chesse Pizza")
      case 2:
        print("\nYou ordered Crust Pizza")
      case 3:
        print("\nYou ordered Dough Pizza")
      case _:
        print("\nWrong number entered")
  case _:
    print("Error")