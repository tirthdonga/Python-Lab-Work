start_leap_year = int(input("Enter the year you want to start from: "))
stop_leap_year = int(input("Enter the year you want to stop: "))

for i in range(start_leap_year, stop_leap_year, 1):
  if i % 4 == 0:
    print(i, end=(" "))
  