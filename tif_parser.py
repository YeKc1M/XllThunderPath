import cv2
import numpy
from PIL import Image

import pix_parser
import tif_parser


class TifParser:

    filePath = ""
    pixs = list()

    def __init__(self, filepath):
        self.filePath = filepath
        img = Image.open(self.filePath)
        imarray = numpy.array(img)
        # print(imarray.shape)
        # print(imarray.shape[0])
        # print(len(imarray))
        # print(imarray)
        # print(imarray[0])
        # for value in imarray[127]:
        #     print(value)
        self.pixs = imarray.copy()

    def generate(self, filepath, maxPath):
        img = Image.new('RGB', (pix_parser.MAX_WIDTH, pix_parser.MAX_HEIGHT))
        for i in range(0, len(self.pixs)):
            for j in range(0, len(self.pixs[i])):
                if self.pixs[i][j] == 255:
                    img.putpixel((j, i), (255, 255, 255))
        for ele in maxPath:
            img.putpixel((ele[0], pix_parser.MAX_HEIGHT - ele[1] - 1), (255, 0, 0))
        img.save(filepath)



def test1():
    tif = TifParser("./skeletonized/S_115.08us.tif")

def test2():
    tif = TifParser("./skeletonized/S_115.08us.tif")
    parser = pix_parser.PixParser(tif.pixs)
    location = parser.findRoot()
    print(location)

def test3():
    tif = TifParser("./skeletonized/S_115.08us.tif")
    parser = pix_parser.PixParser(tif.pixs)
    location = parser.findRoot()
    # print(location)
    parser.DFSRoot(location)
    print(parser.maxPath)
    print(parser.maxLength)

def test4():
    # tif = TifParser("./skeletonized/S_115.08us.tif")
    img = Image.new("RGB", (pix_parser.MAX_WIDTH, pix_parser.MAX_HEIGHT))
    for i in range(0, pix_parser.MAX_HEIGHT):
        for j in range(0, pix_parser.MAX_WIDTH):
            img.putpixel((j, i), (255, 255, 255))
    img.save("temp.tif")


def test5():
    tif = TifParser("./skeletonized/S_115.08us.tif")
    pix = pix_parser.PixParser(tif.pixs)
    root = pix.findRoot()
    pix.DFSRoot(root)
    tif.generate("./temp.tif", pix.maxPath)

if __name__ == '__main__':
    print("hello world!")
    # test1()
    # test2()
    # test3()
    # test4()
    test5()
