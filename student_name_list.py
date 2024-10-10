#1 Creating a list of 20 Student Names

student_names = ["Alucard", "Miya", "Melissa", "Irithel", "Bruno", "Hanabi", "Dyrroth", "Tigreal", "Thamuz", "Layla", "Ling", "Selina", "Karina", "Atlas", "Fanny", "Nana", "Eudora", "Saber", "Zilong", "Freya"]

# A. Print the entire list. 
print(student_names)

# B. Access and print the 15th index.
print("The 15th index is: ", student_names[14])

# C. Update the 12th index to "John".
student_names[11] = "John"
print(student_names)

# D. Delete the 10th index.
del student_names[9]
print(student_names)

# E. Slice the list from index 2 to 5 and print the sliced portion.
print(student_names[1:5])
# OR
print(student_names[1:6])

# F. Print the last index of the list.
print("The last index is: ", student_names[-1])

