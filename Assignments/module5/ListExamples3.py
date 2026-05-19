"""
extend, remove,pop example
"""
fruits= ["apple","banana","mango"]
print(fruits)
#to add single element to list
fruits.append("orange")
# to add list of elements to list
fruits.extend(["kiwi","Guava"])
print(fruits)

#remove deletes first occurrence of item from list
fruits.remove("banana")
print(fruits)

#pop also deletes item . it accepts index to delete items in list. if we don't provide idex,it delets item from last
fruits.pop(1)
print(fruits)

