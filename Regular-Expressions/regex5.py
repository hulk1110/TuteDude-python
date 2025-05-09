import re

string = "It is a Dog 123"
pattern=""
print(re.findall( ".g",string,flags=0))
print(re.findall( "\d",string,flags=0))
print(re.findall( "\D",string,flags=0))
print(re.findall( "\s",string,flags=0))
print(re.findall( "\S",string,flags=0))