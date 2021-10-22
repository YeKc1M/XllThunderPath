import math

MAX_WIDTH = 40
MAX_HEIGHT = 128

class PixParser:

    pix = list()
    path = list()
    maxLength = 0
    maxPath = list()

    def __init__(self, pix):
        self.pix = pix
        self.path = list()
        self.maxLength = 0
        self.maxPath = list()

    def findRoot(self):
        for row in range(0, MAX_HEIGHT):
            for col in range(0, MAX_WIDTH):
                if self.pix[MAX_HEIGHT - row - 1][col] > 0:
                    return [col, row]
        return [-1, -1]

    def DFSRoot(self, rootLocation):
        # self.path.append(rootLocation)
        self.DFS(rootLocation[0], rootLocation[1], 0)

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
        if self.pix[MAX_HEIGHT - 1 - y][x] == 0:
            if length > self.maxLength:
                self.maxLength = length
                self.maxPath = self.path.copy()
            return

        self.path.append([x, y])
        self.DFS(x - 1, y, length + 1)
        self.DFS(x + 1, y, length + 1)
        self.DFS(x, y - 1, length + 1)
        self.DFS(x, y + 1, length + 1)
        self.DFS(x - 1, y - 1, length + math.sqrt(2))
        self.DFS(x - 1, y + 1, length + math.sqrt(2))
        self.DFS(x + 1, y - 1, length + math.sqrt(2))
        self.DFS(x + 1, y + 1, length + math.sqrt(2))
        self.path.remove([x, y])




def test1():
    pix = list()
    for i in range(0, MAX_HEIGHT):
        col = list()
        for j in range(0, MAX_WIDTH):
            col.append(0)
        pix.append(col)
    pix[0][1] = 1
    pix[0][2] = 1
    pix[0][3] = 1
    pix[1][4] = 1
    pix[2][3] = 1
    pix[1][3] = 1
    pixparser = PixParser(pix)
    rootlocation = pixparser.findRoot()
    print(rootlocation)
    pixparser.DFSRoot(rootlocation)
    print(pixparser.maxPath)
    print(pixparser.maxLength)

if __name__ == '__main__':
    print("hello world!")
    test1()