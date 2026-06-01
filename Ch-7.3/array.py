arr = [11, 22, 33, 44, 55]

for i in arr:
  print(i)

sum_arr = []
sum = 0
for i in arr:
  sum += i
  sum_arr.append(sum)

print(sum_arr)
print(sum)
