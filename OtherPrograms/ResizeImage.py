import cv2

path = "Images/"
image = cv2.imread(path + "image.jpg", 0)

scale_percent = 50  # percent of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

cv2.imshow("Resized Image", resized)
cv2.waitKey(0)
