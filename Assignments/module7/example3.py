marks = float(input("Enter your marks: "))

if marks >= 90:
    print("You got grade A")
elif marks >= 80 and marks < 90:
    print("You got grade B")
elif marks >= 70 and marks < 80:
    print("You got grade C")
else:
    print("You Failed!")