from calendar import day_name

name= "John"
age=20
percent= 85.5

student = ["John",20,85.5]
print(type(student))
print(student)

day_name=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
print("last day of week is",day_name[len(day_name)-1])
print(f"last day of week is {day_name[len(day_name)-1]}")


#slicing of list
l1=[3,6,4,7,9,1,8,13,42]
print(l1[1:6:1])
#concatation of list
l2=[0,5]
l3=[1,7,8]
print(l2+l3)
#to repeat list
print(l2*3)
#append() to add item at end of list
fruits =["mango","apple","orange"]
print(fruits)
fruits.append("banana")
print(fruits.append("banana"))
print(fruits)

#insert() to add item before the specified index
list.insert(1,"pineapple")
print(list)

