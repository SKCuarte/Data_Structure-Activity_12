#1. Create a list of 15 countries and the continents they belong to.
continent_country_list = ["Iraq - Asia", "Iran - Asia", "Japan - Asia", "Philippines - Asia", "Thailand - Asia", "Singapore - Asia", "China - Asia", "South Korea - Asia", "Vietnam - Asia", "Yemen - Asia", "France - Europe", "Finland - Europe", "Italy - Europe", "Greece - Europe", "Poland - Europe"]

#2. Print the entire list.
print(continent_country_list)

#3. Access and print the 9th index.
print(continent_country_list[8])

#4. Update the 10th index to "Australia".
continent_country_list[9] = "Australia"
print(continent_country_list)

#5. Delete the 12th index.
del continent_country_list[11]

#6. Slice the list from index 4 to 8.
print(continent_country_list[3:7])
#OR
print(continent_country_list[3:8])

#6. Print the last index.
print("The last index is: ", continent_country_list[-1])