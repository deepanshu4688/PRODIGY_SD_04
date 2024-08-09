import tkinter as tk
from tkinter import messagebox

class SudokuSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")

        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.create_grid()
        
        self.solve_button = tk.Button(root, text="Solve", command=self.solve)
        self.solve_button.grid(row=10, column=0, columnspan=9, sticky=tk.W + tk.E)

    def create_grid(self):
        for row in range(9):
            for col in range(9):
                cell = tk.Entry(self.root, width=5, justify='center', font=('Arial', 12))
                cell.grid(row=row, column=col, padx=2, pady=2)
                self.cells[row][col] = cell

    def get_grid(self):
        grid = []
        for row in range(9):
            grid_row = []
            for col in range(9):
                cell_value = self.cells[row][col].get()
                if cell_value.isdigit():
                    grid_row.append(int(cell_value))
                else:
                    grid_row.append(0)
            grid.append(grid_row)
        return grid

    def set_grid(self, grid):
        for row in range(9):
            for col in range(9):
                if grid[row][col] != 0:
                    self.cells[row][col].delete(0, tk.END)
                    self.cells[row][col].insert(0, str(grid[row][col]))

    def is_safe(self, grid, row, col, num):
        if num in grid[row]:
            return False
        if num in (grid[i][col] for i in range(9)):
            return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if grid[start_row + i][start_col + j] == num:
                    return False

        return True

    def solve_sudoku(self, grid):
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_safe(grid, row, col, num):
                            grid[row][col] = num
                            if self.solve_sudoku(grid):
                                return True
                            grid[row][col] = 0
                    return False
        return True

    def solve(self):
        grid = self.get_grid()
        if self.solve_sudoku(grid):
            self.set_grid(grid)
            messagebox.showinfo("Sudoku Solver", "Sudoku puzzle solved successfully!")
        else:
            messagebox.showerror("Sudoku Solver", "No solution exists for the given Sudoku puzzle.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolverGUI(root)
    root.mainloop()
