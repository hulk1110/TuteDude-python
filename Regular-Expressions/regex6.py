import re

string = "This is Nishant ,Trying to learn Python "

print(re.findall("is*",string))
print(re.findall("is+",string))
print(re.findall("^This",string))
print(re.findall("^T.*",string))
print(re.findall("^This.+",string))
print(re.findall("^This(\S+@\S+)",string))
# print(re.findall("is*",string))
# print(re.findall("is*",string))