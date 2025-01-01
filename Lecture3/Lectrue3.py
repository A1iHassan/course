
num = 10  # Initially, `num` is an integer
print(f"Number: {num}")

num = "hello"  # Now, `num` becomes a string
print(f"String: {num}")




# Strong typing example in Python

num = 10  # Integer
text = "20"  # String

# This will raise a TypeError because Python doesn't allow implicit conversion
result = num + text  # Error: cannot add an integer and a string

# Explicit conversion is required
result = num + int(text)  # Works: 10 + 20 = 30
print(result)
