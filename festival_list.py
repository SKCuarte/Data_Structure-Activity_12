#1. Create a list of 15 festivals around the world.
festival_list = ["Gion Matsuri", "Songkran", "Saint Patrick’s Festival", "Montreux Jazz Festival", "Semana Santa", "Nozawa Onsen Fire Festival", "Cannes Film Festival", "Edinburgh Festival Fringe", "Carnival", "Burning Man", "Oktoberfest", "Mardi Gras", "Dia De Los Muertos", "Snow & Ice Festival", "Glastonbury Festival"]

#2. Print the entire list.
print(festival_list)

#3. Access and print the 7th index.
print(festival_list[6])

#4. Update the 11th index to "Diwali".
festival_list[10] = "Diwali"
print(festival_list)

#5. Delete the 9th index.
del festival_list[8]
print(festival_list)

#6. Slice the list from index 5 to 12.
print(festival_list[4:11])
#OR
print(festival_list[4:12])

#7. Print the last index.
print("The last index is: ", festival_list[-1])
