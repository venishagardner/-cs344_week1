# average_input.py

# step 1 Accumulator for the total of all numbers entered
total = 0

#step 2 Counter for how many numbers the user enters
count = 0

# step 3 Keep asking the user for numbers until they type "q"
while True:
    entry = input("Enter a number or type 'q' to quit: ")

    # step 4 Stop the loop if the user types q
    if entry.lower() == "q":
        break

    # step 5 Convert the input to a number
    number = float(entry)

    # step 6 Add the number to the total
    total += number

    # step 7 Increase the counter
    count += 1

# step 8 Calculate and print the average
if count > 0:
    average = total / count
    print("Average:", average)
else:
    print("No numbers were entered. Average cannot be computed.")
