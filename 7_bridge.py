class Color:
    def __init__(self, value) -> None:
        self.value = value


class Shape:
    def __init__(self, color: Color) -> None:
        self.color = color


class Circle(Shape):
    def __init__(self, color: Color) -> None:
        super().__init__(color)


class Square(Shape):
    def __init__(self, color: Color) -> None:
        super().__init__(color)


blue = Color('blue')
red = Color('red')
blue_circle = Circle(blue)
red_square = Square(red)

print(f'Circle: {blue_circle.color.value}')
print(f'Square: {red_square.color.value}')
