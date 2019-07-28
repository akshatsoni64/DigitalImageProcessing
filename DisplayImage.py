import cv2 as cv

img=cv.imread("image.jpg",1) #second arguement is 1 to read the image in RGB, otherwise if given 0 the image will be read in grayscale

cv.imshow("image",img)
cv.waitKey(0);