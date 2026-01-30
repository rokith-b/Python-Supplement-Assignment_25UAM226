# Problem 50: Convert string to uppercase
# Find and fix the error

text = "python programming"
uppercase_list = []
for char in text:
    if char >= 'a' and char <= 'z':
        uppercase_list.append(chr(ord(char) - 32))
    else:
        uppercase_list.append(char)
uppercase = "".join(uppercase_list)
print(f"Uppercase: {uppercase}")
