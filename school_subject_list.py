#1. Create a list of 12 school subjects.
subject_list = ["Science", "Geography", "History", "Drama", "Computer Science", "Art", "Music", "English", "Writing", "P.E", "TLE", "ICT"]

#2. Print the entire list.
print(subject_list)

#3. Access and print the 6th index.
print(subject_list[5])

#4. Update the 8th index to "Mathematics".
subject_list[7] = "Mathematics"
print(subject_list)

#5. Delete the 4th index.
del subject_list[3]
print(subject_list)

#6. Slice the list from index 2 to 5.
print(subject_list[1:4])
#OR
print(subject_list[1:5])

#7. Print the last index.
print("The last index is: ", subject_list[-1])