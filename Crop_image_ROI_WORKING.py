import cv2
import numpy as np


def read_and_rows_cols():
    img = cv2.imread("Img_0.png")
    rows, cols, _ = img.shape
    return rows, cols


print(read_and_rows_cols())
print("ESC hit, closing program")

img_counter = 0

while True:
    k = cv2.waitKey(1)

    #img = cv2.imread("Img_0.png")
    #img = cv2.imread("Img_1.png")
    #img = cv2.imread("Img_2.1.png")
    #img = cv2.imread("Img_2.2.png")
    #img = cv2.imread("Img_3.png")
    #img = cv2.imread("Img_4.png")
    #img = cv2.imread("Img_5.1.png")
    #img = cv2.imread("Img_5.2.png")
    #img = cv2.imread("Img_6.1.png")
    #img = cv2.imread("Img_6.2.png")
    #img = cv2.imread("Img_7.1.png")
    img = cv2.imread("Img_7.2.png")

    # ROI (Region of interest)
    # roi = img[145:325, 260:440]  # Img_0.png
    # roi = img[180:1165, 420:1150]  # Img_2.1.png
    # roi = img[147:1140, 640:1370]  # Img_2.2.png
    # roi = img[185:970, 215:830]  # Img_3.png
    # roi = img[115:990, 210:820]  # Img_4.png
    # roi = img[118:445, 515:845]  # Img_5.1.png
    # roi = img[118:445, 515:845] Img_5.2.png
    # roi = img[160:377, 247:465]  # Img_6.1.png
    # roi = img[143:375, 233:465]  # Img_6.2.png
    # roi = img[60:240, 210:390]  # Img_7.1.png
    roi = img[87:263, 215:390]  # Img_7.2.png

    if k % 256 == 32:
        # SPACE pressed
        print("SPACE hit, capture image to .png")
        img_name = "Crop_Img_{}.png".format(img_counter)
        cv2.imwrite(img_name, roi)
        print("{} written!".format(img_name))
        img_counter += 1

    cv2.imshow("ROI", roi)
    #cv2.imshow("Show our image", img)

    if k % 256 == 27:
        # ESC pressed
        break

cv2.destroyAllWindows()
