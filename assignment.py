# 1. Python List Transformation
# Task 1: Given the list of grades:

# grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

# Sort the grades in descending order and display the sorted list.
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()
print(grades)

# Task 2: Calculate the average grade and display it.
total = 0
for grade in grades:
    total += grade
print(total/len(grades))

# Task 3: Replace any grade below 80 with the value Failed.
for i, grade in enumerate(grades):
    if grade < 80:
        grades[i] = "Failed"
print(grades)

# 2. Advanced List Methods and Identity Operators
# Task 1: Given the two lists:

# submitted = ["Alice", "Bob", "Charlie", "David"]
# attended = ["Charlie", "Eve", "Alice", "Frank"]

# Find out which students both submitted their assignments and attended the class.
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
submitted_and_attended = []
for student in attended:
    if student in submitted:
        submitted_and_attended.append(student)
print(submitted_and_attended)

# Task 2: Check if the two lists are identical in terms of their content, regardless of order.
submitted.sort()
attended.sort()
if(submitted == attended):
    print("The lists are identical")
else:
    print("The lists are not identical")

# Task 3: Using list methods, remove any student from the attended list who did not submit their assignment.
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
attended_and_not_submitted = []
for student in attended:
    if student not in submitted:
        attended_and_not_submitted.append(student)
print(attended_and_not_submitted)

# 3. Advanced Slicing Techniques
# Task 1: Given the list of temperatures:

# temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

# Extract the temperatures for the second week (7 days) of the month.
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
second_week_temperatures = temperatures[6:13]
print(second_week_temperatures)

# Task 2: Extract all the temperatures above 100.
temperatures_above_100 = []
for temperature in temperatures:
    if temperature > 100:
        temperatures_above_100.append(temperature)
print(temperatures_above_100)

# Task 3: Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list.
temperatures.reverse()
fifth_to_tenth_day_temperatures = temperatures[4:9]
print(fifth_to_tenth_day_temperatures)

# 4. List Comprehensions and Membership Operators
# Task 1: Given the list:

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use a list comprehension to create a new list containing only even numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = [n for n in numbers if n % 2 == 0]
print(new_list)

# Task 2: Use a list comprehension to create a new list containing numbers greater than 5.
new_list = [n for n in numbers if n > 5]
print(new_list)

# Task 3: Check if the number 7 is in the original numbers list.
print(7 in numbers)

# 5. Deep Dive into Python Lists
# Task 1: Given the lists:

# students = ["John", "Doe", "Jane", "Smith"]
# grades = [85, 90, 78, 88]
# activities = ["Football", "Music", "Art", "Dance"]

# Create a new list where each element is a dictionary with keys name, grade, and activity and the corresponding values from the provided lists.
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

new_list = [students, grades, activities]

new_new_list = []
i = 0
while i < len(students):
    if new_list[1][i] >=80:
        new_new_list.append([students[i], grades[i], activities[i]])
    i+=1

print(new_new_list)

# Task 3: For the remaining students, add a new key-value pair in their dictionary: "status": "Passed".
for elem in new_new_list:
    elem[1] = "Passed"

print(new_new_list)