# Problem 9: Find average of numbers in a list
# Find and fix the error

numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
if len(numbers) > 0:
    average = total / len(numbers)
else:
    average = 0
print(f"Average: {average}")
