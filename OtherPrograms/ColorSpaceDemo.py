import cv2
import matplotlib.pyplot as plt
import os


def main():
    path = "Images/"

    imgpath = path + "image.jpg"

    img2 = cv2.imread(imgpath, 1)

    img1 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2LAB)
    img3 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
    img4 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    img5 = cv2.cvtColor(img2, cv2.COLOR_BGR2YCrCb)

    plt.subplot(1, 5, 1)
    plt.imshow(img1)
    plt.title('BGR2RGB')
    plt.xticks([])
    plt.yticks([])

    plt.subplot(1, 5, 2)
    plt.imshow(img2)
    plt.title('BGR2LAB')
    plt.xticks([])
    plt.yticks([])

    plt.subplot(1, 5, 3)
    plt.imshow(img3)
    plt.title('BGR2HSV')
    plt.xticks([])
    plt.yticks([])

    plt.subplot(1, 5, 4)
    plt.imshow(img4)
    plt.title('BGR2GRAY')
    plt.xticks([])
    plt.yticks([])

    plt.subplot(1, 5, 5)
    plt.imshow(img5)
    plt.title('BGR2YCrCb')
    plt.xticks([])
    plt.yticks([])

    plt.savefig("ColorSpaceDemo.png")
    dis = cv2.imread("ColorSpaceDemo.png")
    cv2.imshow("Output", dis)
    cv2.waitKey(0)
    os.remove("ColorSpaceDemo.png")


if __name__ == "__main__":
    main()
