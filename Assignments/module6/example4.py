# sets are collection of items
# they are non sequential collection of items
#comma separated elements eclosed within {}

set1= {7,"parth","agastya","chickoo"}
print(set1)
print(type(set1))

# we can't access items using index
#print(set1[0])

#lenght of set
print(len(set1))

# we can't have duplicate elements in sets, it won't throw any error though
set1.add("agastya")

print(set1)
