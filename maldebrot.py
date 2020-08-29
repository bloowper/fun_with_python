import numpy as np
import cv2
#basic def for img generation
MAX_ITER = 255#for better representation of 255 scale of gay in rgp
RE_START, RE_END = -2, 1
IM_START, IM_END = -1, 1
RE_DISTANCE = RE_END - RE_START
IM_DISTANCE = IM_END - IM_START
partitionCoefficient = 200
imgSize = (partitionCoefficient,int(partitionCoefficient * RE_DISTANCE / IM_DISTANCE))
#creating axes for slice of space
imLineSpaceAxe = np.linspace(IM_START,IM_END,imgSize[0])
reLineSpaceAxe = np.linspace(RE_START,RE_END,imgSize[1])
#creating an image
img = np.zeros((imgSize[0],imgSize[1],1),np.uint8)
for row in range(0,imgSize[0]):
    for col in range(0,imgSize[1]):
        def mandelbrot(c):
            z = np.complex(0,0)
            n = 0
            while np.abs(z)<= 2 and n<MAX_ITER:
                z=np.power(z,2)+c
                n+=1
            return n
        point = np.complex(reLineSpaceAxe[col],imLineSpaceAxe[row])
        speedOfPointSeal = mandelbrot(point)
        img[row][col]=255-speedOfPointSeal
#display
cv2.imshow('set',img)
cv2.imwrite('maldebrot.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()