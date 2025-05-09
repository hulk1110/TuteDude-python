#multi level inheritance

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



class C(B):
    def state6(self):
        print("state 6")
    
    def state7(self):
        print("state 7")


c= C()
c.state1()
c.state2()
c.state3()
c.state4()
c.state5()
c.state6()
c.state7()
    