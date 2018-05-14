"""

CST 205 MultiMediaProject : 
    Image modification functions


"""

from PIL import Image
import cv2
import numpy as np
from matplotlib import pyplot as plt

def grayscale(file): # transform the image color into grey color
    im = Image.open(file)
    grayList = [(int((p[0] + p[1] + p[2])/3),int((p[0] + p[1] + p[2])/3),int((p[0] + p[1] + p[2])/3)) for p in im.getdata()]
    im.putdata(list(grayList))
    return(im)

def negative(file): # inverse the pixel color
    im = Image.open(file)
    negList = [(255-p[0], 255-p[1], 255-p[2]) for p in im.getdata()]
    im.putdata(list(negList))
    return(im)
    
def bigColor(file,col): # intensifies the color asked and decreases the others
    im = Image.open(file)
    colorList = [(int(1.2 * p[col]), int(0.8 * p[(col + 1) % 3]),int(0.8 * p[(col + 2) % 3])) for p in im.getdata()]
    im.putdata(list(colorList))
    return(im)

def darkimg(file): # make the image darker
    im = Image.open(file)
    darkList = [(int(0.5*p[0]), int(0.5*p[1]), int(0.5*p[2])) for p in im.getdata()]
    im.putdata(list(darkList))
    return(im)

def bright(file): # make the image brighter
    im = Image.open(file)
    brightList = [(int(1.5*p[0]), int(1.5*p[1]), int(1.5*p[2])) for p in im.getdata()]
    im.putdata(list(brightList))
    return(im)

def test(file): # Create more contrast between bright pixels and dark pixels
    im = Image.open(file)
    testList = []
    for p in im.getdata():
        avg = (p[0] + p[1] +p[2])/3
        if(avg <= 127):
            newP = (int(0.8*p[0]), int(0.8*p[1]), int(0.8*p[2]))
            testList.append(newP)
        else:
            newP = (int(1.2*p[0]), int(1.2*p[1]), int(1.2*p[2]))
            testList.append(newP)
    im.putdata(list(testList))
    return(im)
            
def nega(file): # small grayscale
    im = Image.open(file)
    negaList = []
    for p in im.getdata():
        avg = (p[0] + p[1] +p[2])/3
        newP = (int((avg + p[0])/ 2), int((avg + p[1])/ 2), int((avg + p[2])/ 2))
        negaList.append(newP)
    im.putdata(list(negaList))
    im.show()

def ok(file): # change pixel color in a fun way
    im = Image.open(file)
    myList = [(int((p[0] + p[1])/2), int((p[1] + p[2])/2), int((p[2] + p[0])/2)) for p in im.getdata()]
    im.putdata(list(myList))
    im.show()


def rotat(file,r): # swap the red, blue and green value
    im = Image.open(file)
    myList = [(p[(0+r)%3],p[(1+r)%3],p[(2+r)%3]) for p in im.getdata()]
    im.putdata(list(myList))
    return(im)

def col(file): # changing color strangely
    im = Image.open(file)
    List = []
    for p in im.getdata():
        maxcol = max(p[0],p[1])
        if(p[2] > maxcol):
            newP = (int(0.9 * p[0]),int(0.9 * p[1]),int(1.1 * p[2]))
            List.append(newP)
        else:
            if(maxcol == p[1]):
                newP = (int(0.9 * p[0]),int(1.1 * p[1]),int(0.9 * p[2]))
                List.append(newP)
            else:
                newP = (int(1.1 * p[0]),int(0.9 * p[1]),int(0.9 * p[2]))
                List.append(newP)
    im.putdata(list(List))
    im.show()

def binarization(file): # transform the image into a black and white image
    im = grayscale(file)
    List = []
    for p in im.getdata():
        if(p[0] < 128):
            newp = (0,0,0)
            List.append(newp)
        else:
            newp = (255,255,255)
            List.append(newp)
    im.putdata(list(List))
    return(im)

def blur(file): # create some blur
    img = cv2.imread(file)
    blur = cv2.GaussianBlur(img,(5,5),0)
    plt.imshow(blur)
    
def edges(file): # Show the edges detected on the image
    img = cv2.imread(file,0)
    edges = cv2.Canny(img,100,200)
    
    im = Image.fromarray(edges)
    return(im)
   
