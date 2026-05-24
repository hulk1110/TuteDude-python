#shallow and deep copy

import copy
l1= [1,2.5,[10,20,30],'python']

#shallow copy
l2= copy.copy(l1)
print(l1)
print(l2)
# their memory location will be differenct
print(id(l1))
print(id(l2))

l1[1]=50
#since this is shallow copy , l2 2nd element will not be changed
print(l1)
print(l2)

l1[2][0]=99
# but inner elements have same address so it also got changed
print(l1)
print(l2)

# deep copy: inner elements also have different address


l3= copy.deepcopy(l1)
print(l3)


d1= {'id':1111,'name':'parth', 'marks':{'com':60,'eng':90}}
d2= copy.deepcopy(d1)
d1['marks']['com']=100
d1['name']='agastya'
print(d1)
print(d2)

