#!/bin/python3

#Lists - []
movies = [" Scream","Evil Dead","Slumber Party Massacre", "You're Next"]
print(movies)#print list
print(movies[0])#Starts at 0
print(movies[2:3])#pick out of list
print(movies[2:])#Start at 
print(movies[:2])#End at 
print(movies[-1])#grabs last item

movies.append("Halloween")#add to end of list
print(movies)
movies.pop()#remove frome end of list
print(movies)
movies.pop(2)#specify add/remove location
print(movies)

#Tuples - Don't Change ()
grades=("A","B","C","D","F")
print (grades[0])

print("\nMy Favorite movie is " + movies[0] + " I give it an " + grades[0] + " rating!"   )
