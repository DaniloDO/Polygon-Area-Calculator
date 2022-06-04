
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        string_rep = f"{self.__class__.__name__}(width={self.width}, height={self.height})"
        return string_rep

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2*self.width) + (2*self.height)

    def get_diagonal(self):
        return (((self.width ** 2) + (self.height ** 2)) ** 0.5)

    def get_picture(self):
        picture = ""

        if(self.height < 50 and self.width < 50):
            for i in range(0, self.height):
                number_width = ('*' * self.width)
                picture += f"{number_width}" + "\n"
            return picture
        else:
            return "Too big for picture."
    
    def get_amount_inside(self, other_class):
        area_local_class = self.get_area()
        area_param_class = other_class.get_area()
        amount = area_local_class / area_param_class

        return int(amount)

class Square(Rectangle):
    def __init__(self, side):
        self.side = side 
        super().__init__(side, side)

    def __repr__(self):
        string_rep = f"{self.__class__.__name__}(side={self.side})"
        return string_rep

    def set_side(self, side):
        self.width = side
        self.height = side
        self.side = side 
    
    def set_width(self, side):
        self.set_side(side)
    
    def set_height(self, side):
        self.set_side(side)
            
