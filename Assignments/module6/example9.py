#operations on dictoneries
from module6.example8 import groceries

marks= {"maths":89.5,"eng":76,"phy":89}
print(marks)

#get()

print(marks.get("maths"))
print(marks.get("computer"))
# marks[computer] throws error
print(marks.get("computer",40))

#memberhip operator
# in checks for key in dictonries
print(40 in marks)
print("maths" in marks)

sem1_marks= {'maths':89.5,'eng':76,'phy':89}
sem2_marks= {'chem':89.5,'bio':76}

sem1_marks.update(sem2_marks)
print(sem1_marks)

groceries_1 = {'milk':30,'rice':40}
groceries_2 = {'rice':30,'pulse':40}
groceries_1.update(groceries_2)
print(groceries_1)

#pop to delete items in dictonaries
groceries_1.pop('milk')
print(groceries_1)