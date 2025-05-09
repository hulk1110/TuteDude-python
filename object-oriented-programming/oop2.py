class const_dest:
    x=0

    def __init__(self,color,type):
        self.color=color
        self.type=type
        print("constructed")

    def __del__(self):
        print("Destructued")


cd = const_dest("black","suv")
print(cd.color)
print(cd.type)
