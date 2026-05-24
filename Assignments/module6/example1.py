#tuple
# sequence of items as a collection
# used when we normally don't modify content example: months of year

t1= ("jan","feb","dec")

t2= ("python",10,1.5,True,[1,2,4],(10,20))
print(t2)
print(t2[0])
print(t2[-1])



t3= (10,20,30)
print(type(t3))

t5= 10,20,30
print(t5)
print(type(t5))
# tuple can be written even without (
listq = [1,2,3,4]
#list to tupple
t = tuple(listq)
print(type(t))

fruits = ("apple","banana","orange")
fruits = list(fruits)
# tupple to list
print(type(fruits))
