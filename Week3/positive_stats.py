# positive_stats.py

# List of integers with positive, negative, and zero values
numbers = [12, -5, 8, 0, -3, 15, 7, -10, 4, 1]

# Counter for positive numbers
positive_count = 0

# Accumulator for the sum of positive numbers
positive_sum = 0

# Loop through the list and accumulate the sum of positive numbers
for number in numbers:
    if number > 0:
        positive_count += 1
        positive_sum += number

# Print the results after the loop is finished
print("Numbers:", numbers)
print("Positive count:", positive_count)
print("Positive sum:", positive_sum)
