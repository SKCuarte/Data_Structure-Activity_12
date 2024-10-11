#1. Create a list of 15 music genres.
music_genre_list = ["Hip hop", "Rock", "Rhythm", "Soul", "Reggae", "Country", "Funk", "Folk", "Disco", "Classical", "Electronic", "Blues", "New Age", "Christian", "Traditional"]

#2. Print the entire list.
print(music_genre_list)

#3. Access and print the 10th index.
print(music_genre_list[9])

#4. Update the 5th index to "Jazz".
music_genre_list[4] = "Jazz"
print(music_genre_list)

#5. Delete the 7th index.
del music_genre_list[6]
print(music_genre_list)

#6. Slice the list from index 3 to 8.
print(music_genre_list[2:7])
#OR
print(music_genre_list[2:8])

#7. Print the last index.
print("The last index is: ", music_genre_list[-1])