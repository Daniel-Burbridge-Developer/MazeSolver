from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__ (self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("Maze Generator")
        self.canvas = Canvas(self.root, width = self.width, height = self.height)
        self.canvas.pack(fill = BOTH, expand = True)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False

    def draw_line(self, line, fill_color = "black"):
        self.line = line
        self.fill_color = fill_color
        line.draw(self.canvas, self.fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def draw(self, canvas, fill_color = "black"):
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill = fill_color, width = 2)
        canvas.pack(fill = BOTH, expand = True)

class Cell:
    def __init__(self, top_left_point, top_right_point, bottom_left_point, bottom_right_point, _win, window):
        self.window = window

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.top_left_point = top_left_point
        self.top_right_point = top_right_point
        self.bottom_left_point = bottom_left_point
        self.bottom_right_point = bottom_right_point

    def draw(self):
        if self.has_left_wall:
            self.window.draw_line(Line(self.bottom_left_point, self.top_left_point))
        if self.has_right_wall:
            self.window.draw_line(Line(self.bottom_right_point, self.top_right_point))
        if self.has_top_wall:
            self.window.draw_line(Line(self.top_left_point, self.top_right_point))
        if self.has_bottom_wall:
            self.window.draw_line(Line(self.bottom_left_point, self.bottom_right_point))


def main():
    win = Window(800, 600)

    cell_one = Cell(Point(10, 10), Point(110, 10), Point(10,110), Point(110, 110), False, win)
    cell_one.draw()
    cell_two = Cell(Point(10, 210), Point(110, 210), Point(10, 310), Point(110, 310), False, win)
    cell_two.draw()


    win.wait_for_close()

if __name__ == "__main__":
    main()