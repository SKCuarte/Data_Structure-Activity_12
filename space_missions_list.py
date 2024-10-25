#1. Create a list of 10 space missions.
mission_list = ["Mercury program", "Gemini program", "Skylab", "Space Shuttle program", "Shuttle-Mir program", "International Space Station", "Commercial Crew Program", "Artemis program", "Biosatellite", "COBE"] 

#2. Print the entire list.
print(mission_list)

#3. Access and print the 7th index.
print(mission_list[6])

#4. Update the 4th index to "Apollo 11".
mission_list[3] = "Apollo 11"
print(mission_list)

#5. Delete the 6th index.
del mission_list[5]
print(mission_list)

#6. Print the last index.
print("The last index is: ", mission_list[-1])