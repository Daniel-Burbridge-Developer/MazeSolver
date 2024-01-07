from tkinter import Tk, BOTH, Canvas
import time

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
    def __init__(self, top_left_point, top_right_point, bottom_left_point, bottom_right_point, _win, window=None):
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

    def draw_move(self, to_cell, undo=False):
        fill_color = "red"
        if undo:
            fill_color = "gray"
        self.window.draw_line(Line(self.get_middle(), to_cell.get_middle()), fill_color)
    def get_middle(self):
        return Point((self.top_left_point.x + self.top_right_point.x) / 2, (self.top_left_point.y + self.bottom_left_point.y) / 2)

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols,cell_size_x, cell_size_y, win=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()

 
    def _create_cells(self):
        cells = []
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                top_left_point = Point(self.x1 + (col * self.cell_size_x), self.y1 + (row * self.cell_size_y))
                top_right_point = Point(top_left_point.x + self.cell_size_x, top_left_point.y)
                bottom_left_point = Point(top_left_point.x, top_left_point.y + self.cell_size_y)
                bottom_right_point = Point(top_right_point.x, bottom_left_point.y)
                cells.append(Cell(top_left_point, top_right_point, bottom_left_point, bottom_right_point, False, self.win))

        self._draw_cells(cells)

    def _draw_cells(self, cells):
        for cell in cells:
            cell.draw()

        # self._animate()
            
    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)
        
def main():
    win = Window(800, 600)
    
     
    maze = Maze(100, 100, 10, 10, 50, 50, win)
 


    win.wait_for_close()

if __name__ == "__main__":
    main()