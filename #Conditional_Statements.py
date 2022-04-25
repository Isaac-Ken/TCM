#!/bin/python3
#Conditional Statements
def drink(money):
	cost=2.50
	tax=((cost*5) /100)
	total=round(cost+tax,2)#rounds down
	print(total)
	if money>=total:
		return "Enjoy your drink :)"
		change_due=(drinkmoney)
	else: 
		return " Sorry, invalid funds :("
print(drink(3))
	
