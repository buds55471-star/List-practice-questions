# Find the largest and smallest numbers in a list.

# Using built-in functions
numbers = [23, 56, 12, 89, 34, 67, 5]

largest = max(numbers)
smallest = min(numbers)

print("Largest number:", largest)
print("Smallest number:", smallest)

# Using sorting
numbers = [23, 56, 12, 89, 34, 67, 5]

numbers.sort()  # sorts ascending
print("Smallest:", numbers[0])
print("Largest:", numbers[-1])

# Using loop
numbers = [23, 56, 12, 89, 34, 67, 5]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest number:", largest)
print("Smallest number:", smallest)
