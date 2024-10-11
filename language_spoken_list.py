#1. Create a list of 20 languages spoken around the world.
language_spoken_list = ["Chinese", "English", "Arabic", "French", "Persian", "German", "Russian", "Malay", "Portuguese", "Italian", "Turkish", "Lahnda", "Tamil", "Urdu", "Korean", "Hindi", "Bengali", "Japanese", "Vietnamese", "Telugu"]

#2. Print the entire list.
print(language_spoken_list)

#3. Access and print the 13th index.
print(language_spoken_list[12])

#4. Update the 10th index to "Spanish".
language_spoken_list[9] = "Spanish"
print(language_spoken_list)

#5. Delete the 16th index.
del language_spoken_list[15]
print(language_spoken_list)

#6. Slice the list from index 6 to 11.
print(language_spoken_list[5:10])
#OR
print(language_spoken_list[4:11])

#7. Print the last index.
print("The last index is: ", language_spoken_list[-1])

