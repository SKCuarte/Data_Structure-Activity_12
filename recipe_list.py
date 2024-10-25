#1. Create a list of 15 recipes.
recipe_list = ["Buttered popcorn", "Masala dosa", "Potato chips", "Seafood paella", "Som tam", "Sinigang", "Adobo", "Chicken rice", "Poutine", "Tacos", "Buttered toast with Marmite", "Stinky tofu", "Marzipan", "Ketchup", "French toast"]

#2. Print the entire list.
print(recipe_list)

#3. Access and print the 12th index.
print(recipe_list[11])

#4. Update the 9th index to "Lasagna".
recipe_list[8] = "Lasagna"
print(recipe_list)

#5. Delete the 11th index.
del recipe_list[10]
print(recipe_list)

#6. Slice the list from index 5 to 10.
print(recipe_list[4:9])
#OR
print(recipe_list[4:10])

#7. Print the last index.
print("The last index is: ", recipe_list[-1])