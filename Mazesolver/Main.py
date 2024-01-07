from tkinter import Tk, BOTH, Canvas
<<<<<<< HEAD
=======
import time
import random
>>>>>>> development

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

<<<<<<< HEAD

def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(0, 0), Point(100, 100)), "red")
=======
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

        self.visited = False
        self._win = _win

    def draw(self):
        bg_color = "grey82"
        if self.window:
            if self.has_left_wall:
                self.window.draw_line(Line(self.bottom_left_point, self.top_left_point))
            else:
                self.window.draw_line(Line(self.bottom_left_point, self.top_left_point), bg_color)
            if self.has_right_wall:
                self.window.draw_line(Line(self.bottom_right_point, self.top_right_point))
            else:
                self.window.draw_line(Line(self.bottom_right_point, self.top_right_point), bg_color)
            if self.has_top_wall:
                self.window.draw_line(Line(self.top_left_point, self.top_right_point))
            else:
                self.window.draw_line(Line(self.top_left_point, self.top_right_point), bg_color)
            if self.has_bottom_wall:
                self.window.draw_line(Line(self.bottom_left_point, self.bottom_right_point))
            else:
                self.window.draw_line(Line(self.bottom_left_point, self.bottom_right_point), bg_color)

    def draw_move(self, to_cell, undo=False):
        fill_color = "blue"
        if undo:
            fill_color = "grey74"
        self.window.draw_line(Line(self.get_middle(), to_cell.get_middle()), fill_color)
    def get_middle(self):
        return Point((self.top_left_point.x + self.top_right_point.x) / 2, (self.top_left_point.y + self.bottom_left_point.y) / 2)

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols,cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()
        self._cells[-1][-1]._win = True
        self._break_entrance_and_exit()
        if seed:
            self.seed = random.seed(seed)

 
    def _create_cells(self):
        self._cells = []
        for row in range(self.num_rows):
            self._cells.append([])
            for col in range(self.num_cols):
                top_left_point = Point(self.x1 + col * self.cell_size_x, self.y1 + row * self.cell_size_y)
                top_right_point = Point(self.x1 + (col + 1) * self.cell_size_x, self.y1 + row * self.cell_size_y)
                bottom_left_point = Point(self.x1 + col * self.cell_size_x, self.y1 + (row + 1) * self.cell_size_y)
                bottom_right_point = Point(self.x1 + (col + 1) * self.cell_size_x, self.y1 + (row + 1) * self.cell_size_y)
                self._cells[row].append(Cell(top_left_point, top_right_point, bottom_left_point, bottom_right_point, False, self.win))

        self._draw_cells()

    def _draw_cells(self):
        for row in self._cells:
            for cell in row:
                if cell.window:
                    cell.draw()
                    self._animate()

        
            
    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False

        self._cells[0][0].draw()
        self._cells[-1][-1].draw()

    def _reset_cells_visisted(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self, i, j):
        cell = self._cells[i][j]
        cell.visited = True
        while not cell._win:
            if cell._win:
                return True
            
            to_visit = []

            # Check if we can move in any direction
            # Check if we can move left
            if j > 0 and not self._cells[i][j-1].visited and not cell.has_left_wall:
                to_visit.append({"left":self._cells[i][j-1]})
            # Check if we can move right
            if j < self.num_cols - 1 and not self._cells[i][j+1].visited and not cell.has_right_wall:
                to_visit.append({"right":self._cells[i][j+1]})
            # Check if we can move up
            if i > 0 and not self._cells[i-1][j].visited and not cell.has_top_wall:
                to_visit.append({"up":self._cells[i-1][j]})
            # Check if we can move down
            if i < self.num_rows - 1 and not self._cells[i+1][j].visited and not cell.has_bottom_wall:
                to_visit.append({"down":self._cells[i+1][j]})
            
            if len(to_visit) == 0:
                return False
            else:
                next_visit = random.choice(to_visit)
                if "left" in next_visit:
                    to_cell = next_visit["left"]
                elif "right" in next_visit:
                    to_cell = next_visit["right"]
                elif "up" in next_visit:
                    to_cell = next_visit["up"]
                elif "down" in next_visit:
                    to_cell = next_visit["down"]
                
                cell.draw_move(to_cell)
                self._animate()

                cell = to_cell
                for a, c in enumerate(self._cells):
                    for b, c2 in enumerate(c):
                        if c2 == cell:
                            i = a
                            j = b
                            break
                if self._solve_r(i, j):
                    return True
        return True

    def _break_walls_r(self, i=0, j=0, debug=False):
        cell = self._cells[i][j]
        cell.visited = True
        while True:
            to_visit = []

            # Check if we can move in any direction
            # Check if we can move left
            if j > 0 and not self._cells[i][j-1].visited:
                to_visit.append({"left":self._cells[i][j-1]})
            # Check if we can move right
            if j < self.num_cols - 1 and not self._cells[i][j+1].visited:
                to_visit.append({"right":self._cells[i][j+1]})
            # Check if we can move up
            if i > 0 and not self._cells[i-1][j].visited:
                to_visit.append({"up":self._cells[i-1][j]})
            # Check if we can move down
            if i < self.num_rows - 1 and not self._cells[i+1][j].visited:
                to_visit.append({"down":self._cells[i+1][j]})
            
            if len(to_visit) == 0:
                cell.draw()
                return
            else:
                next_visit = random.choice(to_visit)
                if "left" in next_visit:
                    cell.has_left_wall = False
                    to_cell = next_visit["left"]
                    to_cell.has_right_wall = False
                elif "right" in next_visit:
                    cell.has_right_wall = False
                    to_cell = next_visit["right"]
                    to_cell.has_left_wall = False
                elif "up" in next_visit:
                    cell.has_top_wall = False
                    to_cell = next_visit["up"]
                    to_cell.has_bottom_wall = False
                elif "down" in next_visit:
                    cell.has_bottom_wall = False
                    to_cell = next_visit["down"]
                    to_cell.has_top_wall = False
                cell.draw()
                to_cell.draw()
                ###DEBUGGER ONLY###
                if debug:
                    cell.draw_move(to_cell)
                ###DEBUGGER ONLY###
                # self._animate()
                cell = to_cell
                for a, c in enumerate(self._cells):
                    for b, c2 in enumerate(c):
                        if c2 == cell:
                            i = a
                            j = b
                            break
                self._break_walls_r(i, j)
            
                
                        

        
def main():
    win = Window(1800, 1250)
    
     
    maze = Maze(100, 100, 20, 24, 50, 50, win)
    maze._break_walls_r(0,0)
    maze._reset_cells_visisted()
    maze.solve()

 


>>>>>>> development
    win.wait_for_close()

if __name__ == "__main__":
    main()