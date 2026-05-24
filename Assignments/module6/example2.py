#operation on tupple

#concatenation example
student_details1 = (1001,"agastya")
student_details2= (78.5,91,83.5,79.5)

student_details= student_details1+student_details2
print(student_details)

#repetation operator example
student_details =student_details1*2
print(student_details)

#memvership operator -- in,not in
print(91 in student_details)
print(1001 in student_details1)

#count
t1= (910,4,1,9,0,3,1)
print(t1.count(91))
print(t1.count(1))

#index
print(t1.index(0))
print(t1.index(1))

#min,max,sum
print(min(t1))
print(max(t1))
print(sum(t1))

