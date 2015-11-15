from graphics import *


class Cell:
    width = 0
    size = 48
    light_color = color_rgb(255, 206, 158)
    dark_color = color_rgb(209, 139, 71)

    def __init__(self, is_light, point_ul):
        point_br = Point(point_ul.getX() + Cell.size, point_ul.getY() + Cell.size)
        self.shape = Rectangle(point_ul, point_br)
        self.shape.setWidth(Cell.width)

        if is_light:
            self.shape.setFill(Cell.light_color)
        else:
            self.shape.setFill(Cell.dark_color)

    def draw(self, window):
        self.shape.draw(window)