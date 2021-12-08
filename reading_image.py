import cv2
import matplotlib.pyplot as plt
# %matplotlib inline

# read images
# img1 = cv2.imread('eye_2.jpg')
# img2 = cv2.imread('eye_1.jpg')

img1 = cv2.imread('odcisk2.jpg')
img2 = cv2.imread('odcisk2.jpg')

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

figure, ax = plt.subplots(1, 2, figsize=(16, 8))

ax[0].imshow(img1, cmap='gray')
ax[1].imshow(img2, cmap='gray')
