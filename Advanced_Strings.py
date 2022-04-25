#!/bin/python3
#Advanced Strings
my_name ="Isaac"
print (my_name[0])
print (my_name[-1])

sentence=" This is a sentence."

print (sentence[:4])

print(sentence.split())

sentence_split = sentence.split()
sentence_join=''.join(sentence_split)
print (sentence_join)

qoute = "OffSec says, \"Try Harder!\" to get your OSCP"
print (qoute)

too_much_space="         Hello       "
print(too_much_space.strip())


print("a" in "Apple")
letter="A"
word="Apple"
print(letter.lower() in word.lower())#Improved 

movie="Scream"
print ("My favorite movie is {}.".format(movie))
