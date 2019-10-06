import os
import cv2
import matplotlib.pyplot as plt

path = "Images/"

image1 = cv2.imread(path + "image.jpg", 1)  # 1 for RGB, 0 for B&W
image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)

image2 = cv2.imread(path + "lena.jpg", 1)
image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)

add = cv2.add(image2, image1)
sub = cv2.subtract(image2, image1)
mul = cv2.multiply(image2, image1)
div = cv2.divide(image2, image1)

plt.subplot(2, 3, 1)
plt.imshow(image1)
plt.title("First Image")

plt.subplot(2, 3, 2)
plt.imshow(image2)
plt.title("Second Image")

plt.subplot(2, 3, 3)
plt.imshow(add)
plt.title("Addition")

plt.subplot(2, 3, 4)
plt.imshow(sub)
plt.title("Subtraction")

plt.subplot(2, 3, 5)
plt.imshow(mul)
plt.title("Multiplication")

plt.subplot(2, 3, 6)
plt.imshow(div)
plt.title("Division")

plt.savefig("ArithmeticOperation.png")
output = cv2.imread("ArithmeticOperation.png")

cv2.imshow("Output", output)
cv2.waitKey(0)
os.remove("ArithmeticOperation.png")
