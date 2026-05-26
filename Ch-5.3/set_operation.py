A = {1, 2 , 3, 4}
B = {3, 4, 5 , 6}

A_union = A.union(B)
print(f"Union of a and b: {A_union}")

A_Intersection = A.intersection(B)
print(f"Intersection of a and b: {A_Intersection}")

A_difference = A.difference(B)
print(f"Difference of a and b: {A_difference}")

'''
Output:
Union of a and b: {1, 2, 3, 4, 5, 6}
Intersection of a and b: {3, 4}
Difference of a and b: {1, 2}
'''

