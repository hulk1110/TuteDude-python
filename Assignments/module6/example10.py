# allowed key in dictionaries  int,float,str,bool, tuple
# not allowed key in dictionaries: list,set,dict because they are mutable

students = {'id':4001,'name':'parth', 'marks':[89.5,71.5,81]}
print(students)
print(students['marks'][1])

students = {'id':4001,'name':'parth', 'marks':{'com':60,'eng':90}}
print(students['marks']['eng'])

print(students.items())