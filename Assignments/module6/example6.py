students1 = {"English","Maths","CS","Chemistry","Physics"}

students2= {"English","Biology"}

# to combine
students3 = students1.union(students2)
print(students3)

#get common
student = students1.intersection(students2)
print(student)


# difference of sets
students= students1.difference(students2)
print(students)

students= students2 - students1
print(students)