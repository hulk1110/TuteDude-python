#nested if example

marks = float(input("Enter your marks: "))
if marks >= 50:
    print("You passed the exam")
    if marks >= 95:
        print("You got A")
    elif marks >= 80:
        print("You got B")
    elif marks >= 70:
        print("You got C")
else:
    print("You did not pass the exam.")