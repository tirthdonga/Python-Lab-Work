fruit = "apple,banana,grapes"

fruit_list = fruit.split(",")

print(fruit_list)

word_list = ["Python", "is", "awesome"]

sentence = " ".join(word_list)

print(sentence)

multiline_str = """Line 1: Hello World!
Line 2: Python is fun.
Line 3: Coding is great."""

lines = multiline_str.splitlines()

for line in lines:
    print(line)

'''
Output:-
['apple', 'banana', 'grapes']
Python is awesome
Line 1: Hello World!
Line 2: Python is fun.
Line 3: Coding is great
'''