from cell import Cell
from graphics import *


class Board:
    border_size = Cell.size // 2
    border_color = color_rgb(180, 110, 40)
    size = 8 * Cell.size + border_size * 2

    def __init__(self):
        self.files = [self.__line(i) for i in range(0, 8)]

    def __line(self, index):
        return [Cell(self.__is_light(index, i),
                     Point(i * Cell.size + Board.border_size,
                           index * Cell.size + Board.border_size)) for i in range(0, 8)]

    # noinspection PyMethodMayBeStatic
    def __is_light(self, f, l):
        return (f + l) % 2 == 0

    def draw(self, window):
        self.__draw_borders(window)
        self.__draw_letters(window)

        for file in self.files:
            for cell in file:
                cell.draw(window)

    # noinspection PyMethodMayBeStatic
    def __draw_letters(self, window):
        half_border = Board.border_size // 2
        half_cell = Cell.size // 2
        letters = [chr(o) for o in range(ord('H'), ord('A') - 1, -1)]

        for i, letter in enumerate(letters):
            t = Text(Point(half_border, Board.border_size + half_cell + Cell.size * i), letter)
            t.setFill(Cell.light_color)
            t.draw(window)

        for i in range(0, 8):
            t = Text(Point(Cell.size * i + half_cell + Board.border_size, Board.size - half_border), i + 1)
            t.setFill(Cell.light_color)
            t.draw(window)

    # noinspection PyMethodMayBeStatic
    def __draw_borders(self, window):
        lb = Rectangle(Point(0, 0), Point(Board.border_size, Board.size))
        lb.setWidth(0)
        lb.setFill(Board.border_color)
        lb.draw(window)

        tb = Rectangle(Point(0, 0), Point(Board.size, Board.border_size))
        tb.setWidth(0)
        tb.setFill(Board.border_color)
        tb.draw(window)

        rb = Rectangle(Point(Board.size - Board.border_size, 0), Point(Board.size, Board.size))
        rb.setWidth(0)
        rb.setFill(Board.border_color)
        rb.draw(window)

        tb = Rectangle(Point(0, Board.size - Board.border_size), Point(Board.size, Board.size))
        tb.setWidth(0)
        tb.setFill(Board.border_color)
        tb.draw(window)