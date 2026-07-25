# Planned functions:

# get_score() - gets the numeric score from the user

# calculate_grade(score) - determines the letter grade

# display_result(score, letter_grade) - displays the result or an error

#Fucntion to get the users's score
def get_score():
    score = int(input("Enter a numeric score from 0 to 100:"))
    return score
#Function to calculate the letter grade
def calculate_grade(score):
    if score < 0 or score > 100:
        return None
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
#Fucntion to display the results
def display_result(score, letter_grade):
    if letter_grade is None:
        print("Error: Please enter a score between 0 and 100.")

    else:

        print("Score:", score, "-> Letter grade:", letter_grade)

# Main function

def main():

    score = get_score()

    letter_grade = calculate_grade(score)

    display_result(score, letter_grade)

# Start the program

main()

    
