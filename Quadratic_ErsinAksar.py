class QuadraticEquation:

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def calculate(self):
        self.disc = self.getDiscriminant()

        self.r1 = self.getRoot1()
        self.r2 = self.getRoot2()

        if(self.disc < 0):
            self.r1 = 0
            self.r2 = 0
            print("root1 and root2 are 0")
        elif(self.disc ==0):
            print(self.r1)
        elif(self.disc>0):
            print(self.r1)
            print(self.r2)
        else:
            print("The equation has no root")


    def getDiscriminant(self):
        disc = self.b**2 - 4*self.a*self.c
        return disc

    def getRoot1(self):
        r1 = (-self.b + (self.b**2 - 4*self.a*self.c)**(1/2)) / (self.a*2)
        return r1

    def getRoot2(self):
        r2 = (-self.b - (self.b**2 - 4*self.a*self.c)**(1/2)) / (self.a*2)
        return r2

