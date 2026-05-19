start_num = int(input("Enter the start number: "))
end_num = int(input("Enter the end number"))

for i in range (start_num, end_num+1):
  for j in range(1, 11):
    print(i, "x", j, "=", i*j)