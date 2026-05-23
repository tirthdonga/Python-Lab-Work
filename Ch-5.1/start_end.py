text = "Hello to the amazing World"

starts_with_hello = text.startswith("Hello")
ends_with_world = text.endswith("World")

if starts_with_hello and ends_with_world:
    print("Yes, it matches both conditions!")
else:
    print("No, it doesn't match.")

# Output: Yes, it matches both conditions!

input_str = "Data123#Science!"

cleaned_str = "".join([c for c in input_str if c.isalpha()])

print(cleaned_str)
# Output: DataScience

original_str = "Python"

reversed_str = original_str[::-1]

print(reversed_str)
# Output: nohtyP