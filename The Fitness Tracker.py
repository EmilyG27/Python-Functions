# Task 1
activity_1 = "Dancing"
activity_2 = "Swimming"
activity_3 = "Biking"

duration_1 = float(10)
duration_2 = float(20)
duration_3 = float(15)

total_calories_burned = (duration_1 + duration_2 + duration_3)*3.5

summary = activity_1 + " for " + str(duration_1) + " minutes.\n"
summary += activity_2 + " for " + str(duration_2) + " minutes.\n"
summary += activity_3 + " for " + str(duration_3) + " minutes."

print(f"{summary}\nYou burned {total_calories_burned} calories today.")