import random

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __repr__(self):
        return f"Cell({self.row}, {self.col})"

class Bulb(Cell):
    def __init__(self, row, col):
        super().__init__(row, col)
        self.is_on = False

    def toggle(self):
        self.is_on = not self.is_on

    def display(self):
        if self.is_on:
            return "*"
        else:
            return "."

class Wall(Cell):
    def __init__(self, row, col):
        super().__init__(row, col)

    def toggle(self):
        return

    def display(self):
        return "|"

class Board():
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.create_grid()

    # creates grid
    def create_grid(self):
        # emtpy list for self.grid
        grid = []
        # create row
        for r in range(self.rows):
            row = []
            # add the bulb at the col in the row
            for c in range(self.cols):
                row.append(Bulb(r, c))
            # appends the row to self.grid
            grid.append(row)
        self.grid = grid

    def place_walls(self, row, col):
        # places a wall at the corrdinates in self.grid
        self.grid[row][col] = Wall(row, col)

    def print_board(self):
        print("  ", end="")
        print(" ".join(str(i) for i in range(self.cols)))
        for r in range(self.rows):
            print(r, end=" ")
            for c in range(self.cols):
                # displays wall or bulb, depends on which gets assigned. 
                print(self.grid[r][c].display(), end=" ")
            print()

    def in_bounds(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols

    def toggle(self, row, col):
        if not self.in_bounds(row, col):
            print("Those numbers are off the board.")
            return
        # calls toggle from bulb
        self.grid[row][col].toggle()
        self.print_board()
    

def game():

    b = None
    while True:
        # # pick num of rows and cols
        try:
            r = int(input("How many rows do you want? Enter a number from 1 through 10."))
            if r <= 0 or r > 10:
                print("Please enter a number from 1 through 10.")
                continue
        except ValueError:
            print("Please enter a number.")
            continue

        try:
            c = int(input("How many columns do you want? Enter a number from 1 through 10."))
            if c <= 0 or c > 10:
                print("Please enter a number from 1 through 10.")
                continue
        except ValueError:
            print("Please enter a number.")
            continue

        # creates a board using board class
        b = Board(r, c)

        # # generates num of wall to create, at most 40% of the squares
        max_walls = (r * c * 40) // 100
        num_of_walls = random.randint(0, max_walls)
    
        # changes bulbs to walls
        spots = [(row, col) for row in range(r) for col in range(c)]
        for row, col in random.sample(spots, num_of_walls):
            b.place_walls(row, col)
        break

    # # # prints board
    b.print_board()

    while True:

        try:
            r = int(input("What row do you want to toggle?"))
            if r < 0:
                print("Please enter a number greater than or equal to 0.")
                continue
        except ValueError:
            print("Please enter a number.")
            continue

        try:
            c = int(input("What column do you want to toggle?"))
            if c < 0:
                print("Please enter a number greater than or equal to 0.")
                continue
        except ValueError:
            print("Please enter a number.")
            continue

        b.toggle(r, c)

        while True:
            keep_playing = input("Do you want to quit?").strip().lower()

            if keep_playing not in ["y", "n"]:
                print("Please enter y or n.")
                continue 
            
            break

        if keep_playing == "y":
            break
    



game()




# if __name__ == "__main__":
#     b = Board(5, 5)
#     b.place_walls(0, 2)
#     b.place_walls(2, 2)
#     b.place_walls(4, 1)
#     b.print_board()
#     b.toggle(1, 1)    # that bulb becomes *
#     # b.toggle(1, 1)    # back to .
#     # b.toggle(0, 2)    # wall stays #
#     # b.toggle(99, 99)  # message, no crash

