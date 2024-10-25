#1. Create a list of 12 land animals and their speeds.
speed_list = ["Mexican pronghor - 88 km/h", "Springbok - 88 km/h", "Thomson’s gazelle - 80-96 km/h", "Blackbuck - 80 km/h", "American quarter horse -70-80 km/h", "Wildebeest - 70-80 km/h", "Brown hare - 70 km/h", "Ostrich - 70 km/h", "Afghan hound = 70 km/h", "Greyhound - 65-70 km/h", "African wild dog - 65-70 km/h", "Coyote - 69 km/h"]

#2. Print the entire list.
print(speed_list)

#3. Access and print the 7th index.
print(speed_list[6])

#4. Update the 9th index to "Cheetah - 120 km/h".
speed_list[8] = "Cheetah - 120 km/h"
print(speed_list)

#5. Delete the 10th index.
del speed_list[9]
print(speed_list)

#6. Slice the list from index 3 to 7.
print(speed_list[2:6])
#OR
print(speed_list[2:7])

#7. Print the last index.
print("The last index is: ", speed_list[-1])
