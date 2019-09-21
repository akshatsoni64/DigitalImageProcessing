import cv2

path = "/home/monster/Pictures/"

image1 = cv2.imread(path + "image.jpg", 1)
image2 = cv2.imread(path + "lena.jpg", 1)

image = image1-image2
# image = cv2.add(image1,image2)
cv2.imshow("Butterfly", image)
cv2.waitKey(0)
