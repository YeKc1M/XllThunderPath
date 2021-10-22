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



def test1():
    tif = TifParser("./skeletonized/S_115.08us.tif")

def test2():
    tif = TifParser("./skeletonized/S_115.08us.tif")
    parser = pix_parser.PixParser(tif.pixs)
    location = parser.findRoot()
    print(location)

if __name__ == '__main__':
    print("hello world!")
    # test1()
    test2()
