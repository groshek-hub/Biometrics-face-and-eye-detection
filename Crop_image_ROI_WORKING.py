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

    img = cv2.imread("Img_0.png")

    # ROI (Region of interest)
    roi = img[145:325, 260:440]

    if k % 256 == 32:
        # SPACE pressed
        print("SPACE hit, capture image to .png")
        img_name = "Crop_Img_{}.png".format(img_counter)
        cv2.imwrite(img_name, roi)
        print("{} written!".format(img_name))
        img_counter += 1

    cv2.imshow("ROI", roi)
    cv2.imshow("Show our image", img)

    if k % 256 == 27:
        # ESC pressed
        break

cv2.destroyAllWindows()
