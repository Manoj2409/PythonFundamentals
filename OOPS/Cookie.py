#Classes
class Cookie:
    def __init__(self,color):
        self.color=color

    def get_color(self):
        return self.color

    def set_color(self,color):
        self.color=color

walnut=Cookie("Brown")
strawberry=Cookie("Pink")

print(walnut.get_color())
walnut.set_color("Orange")
print(walnut.get_color())
print(strawberry.get_color())

