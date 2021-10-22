import math

MAX_WIDTH = 80
MAX_HEIGHT = 240

class PixParser:

    pix = list(list(int))
    path = list(list(int))
    maxLength = 0
    maxPath = list(list(int))

    def __init__(self, pix):
        self.pix = pix
        self.path = list(list(int))
        self.maxLength = 0
        self.maxPath = list(list(int))

    def findRoot(self):
        for row in range(0, MAX_HEIGHT):
            for col in range(0, MAX_WIDTH):
                if self.pix[row][col] == 1:
                    return [col, row]
        return [-1, -1]

    def DFS(self, x, y, length):
        if x < 0 or x >= MAX_WIDTH:
            if length > self.maxLength:
                self.maxLength = length
                self.maxPath = self.path.copy()
            return
        if y < 0 or y >= MAX_HEIGHT:
            if length > self.maxLength:
                self.maxLength = length
                self.maxPath = self.path.copy()
            return
        if [x, y] in self.path:
            if length > self.maxLength:
                self.maxLength = length
                self.maxPath = self.path.copy()
            return
        if self.pix[y][x] == 0:
            if length > self.maxLength:
                self.maxLength = length
                self.maxPath = self.path.copy()
            return

        self.path.append([x - 1, y])
        self.DFS(x - 1, y, length + 1)
        self.path.remove([x - 1, y])

        self.path.append(x + 1, y)
        self.DFS(x + 1, y, length + 1)
        self.path.remove([x + 1, y])

        self.path.append([x, y - 1])
        self.DFS(x, y - 1, length + 1)
        self.path.remove([x, y - 1])

        self.path.append([x, y + 1])
        self.DFS(x, y + 1, length + 1)
        self.path.remove([x, y + 1])

        self.path.append([x - 1, y - 1])
        self.DFS(x - 1, y - 1, length + math.sqrt(2))
        self.path.remove([x - 1, y - 1])

        self.path.append([x - 1, y + 1])
        self.DFS(x - 1, y + 1, length + math.sqrt(2))
        self.path.remove([x - 1, y + 1])

        self.path.append([x + 1, y - 1])
        self.DFS(x + 1, y - 1, length + math.sqrt(2))
        self.path.remove([x + 1, y - 1])

        self.path.append([x + 1, y + 1])
        self.DFS(x + 1, y + 1, length + math.sqrt(2))
        self.path.remove([x + 1, y + 1])
