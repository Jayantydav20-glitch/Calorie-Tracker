# tracker.py
# Name: JAYANT YADAV
# Date: 07/10/2025
# Project: Daily Calorie Tracker

print("Welcome to Daily Calorie Tracker")
print("This program will help you check your calories\n")

# lists for meals and calories
meals = []
calories = []

n = int(input("How many meals you had today? "))

# taking meal names and calories
for i in range(n):
    meal = input("Enter meal name: ")
    cal = float(input("Enter calories for " + meal + ": "))
    meals.append(meal)
    calories.append(cal)

# total and average
total = sum(calories)
avg = total / n

limit = float(input("Enter your daily calorie limit: "))

# checking if over limit
if total > limit:
    print("\nYou have crossed your daily limit!!!")
else:
    print("\nYou are within your daily limit.")

# printing report
print("\n--- Calorie Report ---")
print("Meal\tCalories")
print("----------------------")
for i in range(n):
    print(meals[i], "\t", calories[i])
print("----------------------")
print("Total\t", total)
print("Average\t", avg)

# bonus: save to file with unique name
save = input("\nDo you want to save report? (yes/no): ")

if save.lower() == "yes":
    run_no = input("Enter run number (e.g. 1, 2, 3): ")
    filename = "calorie_log_" + run_no + ".txt"

    f = open(filename, "w")
    f.write("Daily Calorie Report\n")
    f.write("----------------------\n")
    for i in range(n):
        f.write(meals[i] + "\t" + str(calories[i]) + "\n")
    f.write("----------------------\n")
    f.write("Total: " + str(total) + "\n")
    f.write("Average: " + str(avg) + "\n")
    if total > limit:
        f.write("Status: Over limit\n")
    else:
        f.write("Status: Within limit\n")
    f.close()

    print("Report saved to", filename)
else:
    print("Report not saved.")


