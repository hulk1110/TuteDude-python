# comma sepeated key value pair enclosed by {}dataype

#{key1:value1,key2:value2,.....}

groceries= {'milk':'50','biscuits':20,'rice':90,'bread':30}
print(groceries)
print(type(groceries))
print(len(groceries))
#dictonies doesn't have indexing
#print(groceries[1])
print(groceries['milk'])
print(groceries.keys())
# they are mutable
groceries['rice']= 70
print(groceries)
# if we give value to item which is not in dictonieries ,it gets added to dictonary.
groceries['bat']= 10000
print(groceries)