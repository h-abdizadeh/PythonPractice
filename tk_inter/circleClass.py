class circle():
    #property
    radius=1
    pi=3.14

    #method
    def circumfrence(self):
        c=self.radius*2*self.pi
        return c
    
    #constructor
    def __init__(self,r:float):
        self.radius=r

# mycircle=circle()
# mycircle.radius=5
mycircle=circle(7)
print(mycircle.radius)
print(mycircle.pi)
print(mycircle.circumfrence())