
#list are mutable but tuples and string are not

s1= "agastya"
s1.replace("agastya","parth")
print(s1)
s2= s1.replace("agastya","parth")
print(s2)

t1=["orange","mango"]
#id() gives memory address
print(id(t1))
t1.append("mango")
print(id(t1))
print(t1)
# we are modifying the list now
t1[1]="chickoo"
print(t1)
# we cheked they are mutable since there memory address is same
print(id(t1))

t5= ("agastya","parth")
# we won't be able to do and will result in compilation issue
t5[1]="chickoo"
print(t5)