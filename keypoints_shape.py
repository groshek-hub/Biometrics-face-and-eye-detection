import cv2 
import matplotlib.pyplot as plt
# %matplotlib inline

# read images
# img1 = cv2.imread('eye_2.jpg')  
# img2 = cv2.imread('eye_1.jpg') 

img1 = cv2.imread('Img_1.png')  
img2 = cv2.imread('Img_0.png') 


img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#sift
sift = cv2.xfeatures2d.SIFT_create()

keypoints_1, descriptors_1 = sift.detectAndCompute(img1,None)
keypoints_2, descriptors_2 = sift.detectAndCompute(img2,None)

print(len(keypoints_1))
print(len(keypoints_2))