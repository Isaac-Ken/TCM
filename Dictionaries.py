#!/bin/python3
#Dictionaries -key/value pairs{}
drinks={"Cola":2,"Root Beer":2,"Orange":3,"Lemon Lime":4}#drink name is key, number is value
print(drinks)


employees={"Finance":["Alex","Stan","Jerry"], "IT": ["Roger","Mary"], "HR" :["Steve"]}
print(employees)

employees["Legal"]=["Jeff"] #add new key value pair
print(employees)

employees.update({"Sales": ["Lisa","Jim"]})#add new key value pair
print(employees)

drinks ["Cola"]=1
print (drinks)
print (drinks.get("Cola"))
