class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __repr__(self):
        return f"Cell({self.row}, {self.col})"



if __name__ == "__main__":
    c = Cell(1, 2)
    print(c)

