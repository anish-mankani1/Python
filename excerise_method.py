class circle:
    pi=3.14
    def __init__(self,radius,area) -> None:
     self.radius=radius
     self.area=area*self.pi*radius*radius#2*3.14*4*4

    def circumference(self):
        return 2*self.pi*self.radius*self.radius
circle_1=circle(4,2)
print(circle_1.radius)
print(circle_1.area)
print(circle_1.circumference())