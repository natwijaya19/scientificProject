#%%
class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info(self):
        print("A polygon is a two dimensional shape "
              "with straight lines")

    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter

class Triangle(Polygon):
    def display_info(self):
        print("A triangle is a polygon with 3 edges")

class Quadrilateral (Polygon):
    def display_info(self):
        print("A quadrilateral is a polygo with 4 edges")


#%%
t1 = Triangle([5,6,7])
perimeter = t1.get_perimeter()
print("The perimeter is", perimeter)
print(t1.display_info())

