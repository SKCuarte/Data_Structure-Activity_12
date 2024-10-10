#1. Create a list of 20 movie titles.
movie_list = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "The Godfather Part II", "12 Angry Men", "The Lord of the Rings: The Return of the King", "Schindler's List", "Pulp Fiction", "The Lord of the Rings: The Fellowship of the Ring", "The Good, the Bad and the Ugly", "Forrest Gump", "The Lord of the Rings: The Two Towers", "Fight Club", "Avengers", "Star Wars: Episode V - The Empire Strikes Back", "The Matrix", "Goodfellas", "One Flew Over the Cuckoo's Nest", "Interstellar", "Se7en"]

#2. Print the entire list.
print(movie_list)

#3. Access and print the 12th index.
print(movie_list[11])

#4. Update the 15th index to "Inception".
movie_list[14] = "Inception"
print(movie_list)

#5. Delete the 18th index.
del movie_list[17]
print(movie_list)

#6. Slice the list from index 8 to 13.
print(movie_list[7:12])
#OR
print(movie_list[7:13])

#7. Print the last index.
print("The last index is: ", movie_list[-1])




