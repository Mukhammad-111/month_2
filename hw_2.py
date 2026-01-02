class Figure:
    unit = 'см'

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass


class Square(Figure):
    def __init__(self, side_length):
        super(Square, self).__init__()
        self.__side_length = side_length

    def calculate_area(self):
        return self.__side_length * self.__side_length

    def info(self):
        print(f'Square side length: {self.__side_length}{Figure.unit}, '
              f'area: {self.calculate_area()}{Figure.unit}')


class Rectangle(Figure):
    def __init__(self, length, width):
        super(Rectangle, self).__init__()
        self.__length = length
        self.__width = width

    def calculate_area(self):
        return self.__length * self.__width

    def info(self):
        print(f'Rectangle length: {self.__length}{Figure.unit}, '
              f'width: {self.__width}{Figure.unit}, area: {self.calculate_area()}{Figure.unit}')


my_list = [Square(7), Square(4), Rectangle(3,8), Rectangle(5, 6),
           Rectangle(9, 6)]

for i in my_list:
    i.info()