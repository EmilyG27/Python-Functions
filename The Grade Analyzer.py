# Task 1
grades = [100, 95, 90, 85, 80]
average = sum(grades)/len(grades)
print(f"The average grade is {average}")

# Task 2
highest_grade = max(grades)
print(f"The highest grade is {highest_grade}")
lowest_grade = min(grades)
print(f"The lowest grade is {lowest_grade}")

# Task 3
if average >= 90:
    print("Your letter grade is 'A'")
elif grades >= 80 and grades < 90:
    print("Your letter grade is 'B'")
elif grades >= 70 and grades < 80:
    print("Your letter grade is 'C'")
elif grades >= 60 and grades < 70:
    print("Your letter grade is 'D'")
else:
    print("Your letter grade is'F'")