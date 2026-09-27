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
            print("*")
        else:
            print(".")

class Wall(Cell):
    def __init__(self, row, col):
        super().__init__(row, col)

    def toggle(self):
        return

    def display(self):
        return "#"

if __name__ == "__main__":
    c = Cell(1, 2)
    print(c)
    b = Bulb(0, 0)
    print(b.display())
    b.toggle()
    print(b.display())
    b.toggle()
    print(b.display())

