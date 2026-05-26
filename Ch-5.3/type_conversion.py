string = "123"
print(f"String to integer: {int(string)} {type(string)}")

list_ = [1, 2, 3]
print(f"List to Tuple: {tuple(list_)} {type(list_)}")

tuple_ = (1, 2, 3)
print(f"Tuple to List: {list(tuple_)} {type(tuple_)}")

pair = [(1, 'A'), (2, 'B')]
print(f"List to Dictonary: {dict(pair)}")

'''
Ouput:
String to integer: 123 <class 'str'>
List to Tuple: (1, 2, 3) <class 'list'>
Tuple to List: [1, 2, 3] <class 'tuple'>
List to Dictonary: {1: 'A', 2: 'B'}
'''

