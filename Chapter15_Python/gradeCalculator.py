#Calculate the letter grade based on a numeric score. A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: below 60.

score = int(input("Enter the numeric score: "))
if score >= 90:
    print("The letter grade is: A")
elif score >= 80:
    print("The letter grade is: B")
elif score >= 70:
    print("The letter grade is: C")
elif score >= 60:
    print("The letter grade is: D")
else:
    print("The letter grade is: F")
