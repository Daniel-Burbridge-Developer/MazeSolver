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


def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(0, 0), Point(100, 100)), "red")
    win.wait_for_close()

if __name__ == "__main__":
    main()