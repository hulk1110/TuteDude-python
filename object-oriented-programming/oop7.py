#single level inheritance
class A:
    def state1(self):
        print("state 1")
    
    def state2(self):
        print("state 2")
    
    def state3(self):
        print("state 3")


class B(A):
    def state4(self):
        print("state 4")
    
    def state5(self):
        print("state 5")
    

a= A()
a.state1()
b= B()
b.state2()
b.state3()
b.state4()
b.state5()