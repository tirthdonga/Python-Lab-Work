from operator import itemgetter 
students = []
while True:

  print("Press 1 To Enter Student Information")
  print("Press 2 To Get all Student Information")
  print("Press 3 To Get Average Score Of all Student")
  print("Press 4 To Update Student Information")
  print("Press 5 To Delete Student Information")
  print("Press 6 To Print Student Who Score Higher Than 80")
  print("Press 7 To Sort Than By Score")
  print("Press 8 To get Student With Highest Score")
  print("Press 9 To Create A Report")
  print("Press 10 To See How Many Student Got Each Grade\n")
  
  btn1 = int(input("Please Enter The Number: "))
  print()

  match btn1:

    case 1:
      id = int(input("Enter The ID: "))
      name = input("Enter The Name: ")
      score = int(input("Enter The Score: "))

      student = {'id' : id, 'name' : name, 'score' : score}
      students.append(student)
      print("Data Added Sucessfully\n")

    case 2: 
      if not students:
        print("No Data Detected\n")
      for stu in students:
        print(f"ID: {stu['id']} | Name: {stu['name']} | Score: {stu['score']}\n")

    case 3:
      total_score = 0
      if len(students) > 0:
        for stu in students:
          total_score += stu['score']

        average = total_score / len(students)
        print(f"Average Score is: {average}\n")
      else:
        print("List Is Empty")

    case 4:
      grid = int(input("Please Enter Your GRID: "))
      found = False

      for stu in students:
        if stu['id'] == grid:
          found = True
          while True:
            print("Press 1 To Update Name")
            print("Press 2 To Update Score")
            print("Press 0 To Exit")

            btn2 = int(input("Please Enter the Number: "))
            match btn2:
              case 1:
                new_name = input("Enter New Name: ")
                stu['name'] = new_name
              case 2:
                new_score = input("Enter New Score: ")
                stu['score'] = new_score
              case 0:
                break
              case _: 
                print("Invalid Number Entered")
            print("Data Update Successfully")
      if found == False:
        print("No Data Found")
  
    case 5:
      grid = int(input("Please Enter Your GRID: "))
      found = False

      for stu in students:
        if stu['id'] == grid:
          found = True
          students.remove(stu)
          print("Data Delete Successfully")
          print()

    case 6:
      print("This Are The Student Higher Score Than 80")
      found = True

      for stu in students:
        if stu['score'] > 80:
          print(f"ID: {stu['id']} | Name: {stu['name']} | Score: {stu['score']}")
          found = True
        
      if not found:
        print("No Student Found Score Higher Than 80")

    case 7: 
      from operator import itemgetter 
      if students:
        students.sort(key=itemgetter('score'), reverse=True)
        print("Sorted successfully using itemgetter!")
      else:
        print("The list is empty.")

    case 8: 
      if not students:
        print("No Data Detected")
      else:
        top_student = students[0]
        for stu in students:
          if stu['score'] > top_student['score']:
            top_student = stu
            print(f"Highest Score: {top_student['score']} (Name: {top_student['name']})")

    case 9:
      for stu in students:
        if stu['score'] >= 90:
          stu['grade'] = 'A'  # This adds the 'grade' key to the current student
        elif stu['score'] >= 80:
          stu['grade'] = 'B'
        elif stu['score'] <= 79:
          stu['grade'] = 'C'
        else:
          stu['grade'] = 'F'

      if not students:
        print("No Data Detected\n")
      for stu in students:
        print(f"ID: {stu['id']} | Name: {stu['name']} | Score: {stu['score']} | Grade : {stu['grade']}\n")
    case 10:
      grade_a = 0
      grade_b = 0
      grade_c = 0
      grade_f = 0
      for stu in students:
        score = stu['score']
        if score == 'A':
          grade_a += 1
        elif score == 'B':
          grade_b += 1
        elif score == 'C':
          grade_c += 1
        else:
          grade_f += 1
          

      print(f"Grade A (90+): {grade_a}")
      print(f"Grade B (80-89): {grade_b}")
      print(f"Grade C (70-79): {grade_c}")
      print(f"Grade F (Below 70): {grade_f}")

    case _:
      print("Invalid Number Entered")
