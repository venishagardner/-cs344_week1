#Enter the a score from 0 to 100
score=int(input(" Enter a numeric score from 0 to 100:"))
if score < 0 or score > 100:
     print("Error: Please enter a score between 0 and 100.")

elif score >= 90:

    letter_grade = "A"

elif score >= 80:

    letter_grade = "B"

elif score >= 70:

    letter_grade = "C"

elif score >= 60:

    letter_grade = "D"

else:

    letter_grade = "F"

# Print the result if the score was valid

if 0 <= score <= 100:

    print("Score:", score, "-> Letter grade:", letter_grade)
