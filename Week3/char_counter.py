# char_counter.py

# Ask the user to enter a line of text

text = input("Enter a line of text: ")

# Ask the user to enter a character to search for

character = input("Enter a character to search for: ")

# Counter for the number of times the character appears

count = 0

# Loop through each character in the text

for letter in text:

    # Check if the current letter matches the character

    if letter == character:

        count += 1

# Print the final result

print("The character", character, "appears", count, "time(s).")
