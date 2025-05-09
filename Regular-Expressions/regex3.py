import re

pattern = "apple"

if re.search(pattern,"ballapple"):
    print ("True")
else:
    print ("False")