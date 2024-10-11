#1. Create a list of 15 Pokémon names.
pokemon_list = ["Torchic", "Combusken", "Blaziken", "Mega Blaziken", "Gible", "Gabite", "Garchomp", "Mega Garchomp", "Riolu", "Lucario", "Mega Lucario", "Beldum", "Metang", "Metagross", "Mega Metagross"]

#2. Print the entire list.
print(pokemon_list)

#3. Access and print the 9th index.
print(pokemon_list[8])

#4. Update the 12th index to "Pikachu".
pokemon_list[11] = "Pikachu"
print(pokemon_list)

#5. Delete the 10th index.
del pokemon_list[9]
print(pokemon_list)

#6. Slice the list from index 4 to 7.
print(pokemon_list[3:6])
#OR
print(pokemon_list[3:7])

#7. Print the last index.
print("The last index is: ", pokemon_list[-1])

