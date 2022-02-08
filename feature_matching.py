# pip install matplotlib
import cv2
import matplotlib.pyplot as plt

# read images
# img1 = cv2.imread('Crop_Img_0.png') # Zdjecie Pawel 0
# img2 = cv2.imread('Crop_Img_1.png') # Zdjecie Pawel 1

# img1 = cv2.imread('Crop_Img_5.1.png') #Zdjecie Emil 5.1
# img2 = cv2.imread('Crop_Img_5.2.png')   #Zdjecie Emil 5.2

# img1 = cv2.imread('Crop_Img_6.1.png') #Zdjecie Kacper 6.1
# img2 = cv2.imread('Crop_Img_6.2.png')   #Zdjecie Kacper 6.2

# img1 = cv2.imread('Crop_Img_2.1.png') #Zdjecie Mezczyzny 2.1
# img2 = cv2.imread('Crop_Img_2.2.png') #Zdjecie Mezczyzny 2.2

# img1 = cv2.imread('Crop_Img_3.png') #Zdjecie Kobiety 3
# img2 = cv2.imread('Crop_Img_4.png') #Zdjecie Mezczyzny 4

# img1 = cv2.imread('Crop_Img_2.1.png') #Zdjecie Mezczyzny 2.1
# img2 = cv2.imread('Crop_Img_3.png')   #Zdjecie Kobiety 3

# img1 = cv2.imread('Crop_Img_2.2.png') #Zdjecie Mezczyzny 2.2
# img2 = cv2.imread('Crop_Img_3.png')   #Zdjecie Kobiety 3

# img1 = cv2.imread('Crop_Img_2.1.png') #Zdjecie Mezczyzny 2.1
# img2 = cv2.imread('Crop_Img_4.png')   #Zdjecie Mezczyzyny 4

# img1 = cv2.imread('Crop_Img_2.2.png') #Zdjecie Mezczyzny 2.2
# img2 = cv2.imread('Crop_Img_4.png')   #Zdjecie Mezczyzyny 4

# img1 = cv2.imread('Crop_Img_0.png')    #Zdjecie Pawel 0
# img2 = cv2.imread('Crop_Img_3.png')    #Zdjecie Kobiety 3

# img1 = cv2.imread('Crop_Img_0.png')    #Zdjecie Pawel 0
# img2 = cv2.imread('Crop_Img_4.png')    #Zdjecie Mezczyzny 4

# img1 = cv2.imread('Crop_Img_0.png') #Zdjecie Pawel 0
# img2 = cv2.imread('Crop_Img_5.1.png')   #Zdjecie Emil 5.1

# img1 = cv2.imread('Crop_Img_0.png') #Zdjecie Pawel 0
# img2 = cv2.imread('Crop_Img_5.2.png')   #Zdjecie Emil 5.2

# img1 = cv2.imread('Crop_Img_1.png') #Zdjecie Pawel 1
# img2 = cv2.imread('Crop_Img_5.1.png')   #Zdjecie Emil 5.1

# img1 = cv2.imread('Crop_Img_1.png') #Zdjecie Pawel 1
# img2 = cv2.imread('Crop_Img_5.2.png')   #Zdjecie Emil 5.2

# img1 = cv2.imread('Crop_Img_3.png') #Zdjecie Kobiety 3
# img2 = cv2.imread('Crop_Img_5.1.png')   #Zdjecie Emil 5.1

# img1 = cv2.imread('Crop_Img_3.png') #Zdjecie Kobiety 3
# img2 = cv2.imread('Crop_Img_5.2.png')   #Zdjecie Emil 5.2

# img1 = cv2.imread('Crop_Img_4.png') #Zdjecie Mezczyzny 4
# img2 = cv2.imread('Crop_Img_5.1.png')   #Zdjecie Emil 5.1

# img1 = cv2.imread('Crop_Img_4.png') #Zdjecie Mezczyzny 4
# img2 = cv2.imread('Crop_Img_5.2.png')   #Zdjecie Emil 5.2

# img1 = cv2.imread('Crop_Img_0.png') #Zdjecie Pawel 0
# img2 = cv2.imread('Crop_Img_6.1.png')   #Zdjecie Kacper 6.1

# img1 = cv2.imread('Crop_Img_0.png') #Zdjecie Pawel 0
# img2 = cv2.imread('Crop_Img_6.2.png')   #Zdjecie Kacper 6.2

# img1 = cv2.imread('Crop_Img_1.png') #Zdjecie Pawel 1
# img2 = cv2.imread('Crop_Img_6.1.png')   #Zdjecie Kacper 6.1

# img1 = cv2.imread('Crop_Img_1.png') #Zdjecie Pawel 1
# img2 = cv2.imread('Crop_Img_6.2.png')   #Zdjecie Kacper 6.2

# img1 = cv2.imread('Crop_Img_5.1.png') #Zdjecie Emil 5.1
# img2 = cv2.imread('Crop_Img_6.1.png')   #Zdjecie Kacper 6.1

# img1 = cv2.imread('Crop_Img_5.1.png') #Zdjecie Emil 5.1
# img2 = cv2.imread('Crop_Img_6.2.png')   #Zdjecie Kacper 6.2

# img1 = cv2.imread('Crop_Img_5.2.png') #Zdjecie Emil 5.2
# img2 = cv2.imread('Crop_Img_6.1.png')   #Zdjecie Kacper 6.1

# img1 = cv2.imread('Crop_Img_5.2.png') #Zdjecie Emil 5.2
# img2 = cv2.imread('Crop_Img_6.2.png')   #Zdjecie Kacper 6.2

# img1 = cv2.imread('Crop_Img_3.png') #Zdjecie Kobiety 3
# img2 = cv2.imread('Crop_Img_6.1.png')   #Zdjecie Kacper 6.1

# img1 = cv2.imread('Crop_Img_3.png') #Zdjecie Kobiety 3
# img2 = cv2.imread('Crop_Img_6.2.png')   #Zdjecie Kacper 6.2

# img1 = cv2.imread('Crop_Img_4.png') #Zdjecie Mezczyzny 4
# img2 = cv2.imread('Crop_Img_6.1.png')   #Zdjecie Kacper 6.1

# img1 = cv2.imread('Crop_Img_4.png') #Zdjecie Mezczyzny 4
# img2 = cv2.imread('Crop_Img_6.2.png')   #Zdjecie Kacper 6.2

# 05.01.22r.
# img1 = cv2.imread('Crop_Img_7.1.png')  # Zdjecie Kuba 7.1
# img2 = cv2.imread('Crop_Img_7.2.png')  # Zdjecie Kuba 7.2

# img1 = cv2.imread('Crop_Img_7.1.png')  # Zdjecie Kuba 7.1
# img2 = cv2.imread('Crop_Img_0.png')  # Zdjecie Pawel 0

# img1 = cv2.imread('Crop_Img_7.1.png')  # Zdjecie Kuba 7.1
# img2 = cv2.imread('Crop_Img_1.png')  # Zdjecie Pawel 1

# img1 = cv2.imread('Crop_Img_7.2.png')  # Zdjecie Kuba 7.2
# img2 = cv2.imread('Crop_Img_0.png')  # Zdjecie Pawel 0

# img1 = cv2.imread('Crop_Img_7.2.png')  # Zdjecie Kuba 7.2
# img2 = cv2.imread('Crop_Img_1.png')  # Zdjecie Pawel 1

# img1 = cv2.imread('Crop_Img_7.1.png')  # Zdjecie Kuba 7.1
# img2 = cv2.imread('Crop_Img_5.1.png')  # Zdjecie Emil 5.1

# img1 = cv2.imread('Crop_Img_7.1.png')  # Zdjecie Kuba 7.1
# img2 = cv2.imread('Crop_Img_5.2.png')  # Zdjecie Emil 5.2

# img1 = cv2.imread('Crop_Img_7.2.png')  # Zdjecie Kuba 7.2
# img2 = cv2.imread('Crop_Img_5.1.png')  # Zdjecie Emil 5.1

# img1 = cv2.imread('Crop_Img_7.2.png')  # Zdjecie Kuba 7.2
# img2 = cv2.imread('Crop_Img_5.2.png')  # Zdjecie Emil 5.2

# img1 = cv2.imread('Crop_Img_7.1.png')  # Zdjecie Kuba 7.1
# img2 = cv2.imread('Crop_Img_6.1.png')  # Zdjecie Kacper 6.1

# img1 = cv2.imread('Crop_Img_7.1.png')  # Zdjecie Kuba 7.1
# img2 = cv2.imread('Crop_Img_6.2.png')  # Zdjecie Kacper 6.2

# img1 = cv2.imread('Crop_Img_7.2.png')  # Zdjecie Kuba 7.2
# img2 = cv2.imread('Crop_Img_6.1.png')  # Zdjecie Kacper 6.1

# img1 = cv2.imread('Crop_Img_7.2.png')  # Zdjecie Kuba 7.2
# img2 = cv2.imread('Crop_Img_6.2.png')  # Zdjecie Kacper 6.2

# img1 = cv2.imread('Crop_Img_7.1.png')  # Zdjecie Kuba 7.1
# img2 = cv2.imread('Crop_Img_3.png')  # Zdjecie Kobieta 3

# img1 = cv2.imread('Crop_Img_7.1.png')  # Zdjecie Kuba 7.1
# img2 = cv2.imread('Crop_Img_4.png')  # Zdjecie Mezczyzna 4

# img1 = cv2.imread('Crop_Img_7.1.png')  # Zdjecie Kuba 7.1
# img2 = cv2.imread('Crop_Img_2.1.png')  # Zdjecie Mezczyzna 2.1

# img1 = cv2.imread('Crop_Img_7.1.png')  # Zdjecie Kuba 7.1
# img2 = cv2.imread('Crop_Img_2.2.png')  # Zdjecie Mezczyzna 2.2

# img1 = cv2.imread('Crop_Img_7.2.png')  # Zdjecie Kuba 7.2
# img2 = cv2.imread('Crop_Img_3.png')  # Zdjecie Kobieta 3

# img1 = cv2.imread('Crop_Img_7.2.png')  # Zdjecie Kuba 7.2
# img2 = cv2.imread('Crop_Img_4.png')  # Zdjecie Mezczyzna 4

# img1 = cv2.imread('Crop_Img_7.2.png')  # Zdjecie Kuba 7.2
# img2 = cv2.imread('Crop_Img_2.1.png')  # Zdjecie Mezczyzna 2.1

# img1 = cv2.imread('Crop_Img_7.2.png')  # Zdjecie Kuba 7.2
# img2 = cv2.imread('Crop_Img_2.2.png')  # Zdjecie Mezczyzna 2.2

# img1 = cv2.imread('Crop_Img_0.png')  # Zdjecie Pawel 0
# img2 = cv2.imread('Crop_Img_2.1.png')  # Zdjecie Mezczyzna 2.1

# img1 = cv2.imread('Crop_Img_0.png')  # Zdjecie Pawel 0
# img2 = cv2.imread('Crop_Img_2.2.png')  # Zdjecie Mezczyzna 2.2

# img1 = cv2.imread('Crop_Img_1.png')  # Zdjecie Pawel 1
# img2 = cv2.imread('Crop_Img_2.1.png')  # Zdjecie Mezczyzna 2.1

# img1 = cv2.imread('Crop_Img_1.png')  # Zdjecie Pawel 1
# img2 = cv2.imread('Crop_Img_2.2.png')  # Zdjecie Mezczyzna 2.2

# img1 = cv2.imread('Crop_Img_1.png')  # Zdjecie Pawel 1
# img2 = cv2.imread('Crop_Img_3.png')  # Zdjecie Kobieta 3

# img1 = cv2.imread('Crop_Img_1.png')  # Zdjecie Pawel 1
# img2 = cv2.imread('Crop_Img_4.png')  # Zdjecie Mezczyzna 4

# img1 = cv2.imread('Crop_Img_1.png')  # Zdjecie Pawel 1
# img2 = cv2.imread('Crop_Img_7.1.png')  # Zdjecie Kuba 7.1

# img1 = cv2.imread('Crop_Img_1.png')  # Zdjecie Pawel 1
# img2 = cv2.imread('Crop_Img_7.2.png')  # Zdjecie Kuba 7.2

# img1 = cv2.imread('Crop_Img_5.1.png')  # Zdjecie Emil 5.1
# img2 = cv2.imread('Crop_Img_2.1.png')  # Zdjecie Mezczyzna 2.1

# img1 = cv2.imread('Crop_Img_5.1.png')  # Zdjecie Emil 5.1
# img2 = cv2.imread('Crop_Img_2.2.png')  # Zdjecie Mezczyzna 2.2

# img1 = cv2.imread('Crop_Img_5.2.png')  # Zdjecie Emil 5.2
# img2 = cv2.imread('Crop_Img_2.1.png')  # Zdjecie Mezczyzna 2.1

# img1 = cv2.imread('Crop_Img_5.2.png')  # Zdjecie Emil 5.2
# img2 = cv2.imread('Crop_Img_2.2.png')  # Zdjecie Mezczyzna 2.2

# img1 = cv2.imread('Crop_Img_6.1.png')  # Zdjecie Kacper 6.1
# img2 = cv2.imread('Crop_Img_2.1.png')  # Zdjecie Mezczyzna 2.1

# img1 = cv2.imread('Crop_Img_6.1.png')  # Zdjecie Kacper 6.1
# img2 = cv2.imread('Crop_Img_2.2.png')  # Zdjecie Mezczyzna 2.2

# img1 = cv2.imread('Crop_Img_6.1.png')  # Zdjecie Kacper 6.1
# img2 = cv2.imread('Crop_Img_3.png')  # Zdjecie Kobieta 3

# img1 = cv2.imread('Crop_Img_6.1.png')  # Zdjecie Kacper 6.1
# img2 = cv2.imread('Crop_Img_4.png')  # Zdjecie Mezczyzna 4

# img1 = cv2.imread('Crop_Img_6.2.png')  # Zdjecie Kacper 6.2
# img2 = cv2.imread('Crop_Img_2.1.png')  # Zdjecie Mezczyzna 2.1

# img1 = cv2.imread('Crop_Img_6.2.png')  # Zdjecie Kacper 6.2
# img2 = cv2.imread('Crop_Img_2.2.png')  # Zdjecie Mezczyzna 2.2

# img1 = cv2.imread('Crop_Img_6.2.png')  # Zdjecie Kacper 6.2
# img2 = cv2.imread('Crop_Img_3.png')  # Zdjecie Kobieta 3

# img1 = cv2.imread('Crop_Img_6.2.png')  # Zdjecie Kacper 6.2
# img2 = cv2.imread('Crop_Img_4.png')  # Zdjecie Mezczyzna 4

# Ada 6.01.22r.
#img1 = cv2.imread('Crop_Img_8.1.png')  # Zdjecie Ada 8.1
#img2 = cv2.imread('Crop_Img_8.2.png')  # Zdjecie Ada 8.2

img1 = cv2.imread('Crop_Img_8.2.png')  # Zdjecie Ada 8.2
img2 = cv2.imread('Crop_Img_8.3.png')  # Zdjecie Ada 8.3

#img1 = cv2.imread('Crop_Img_8.1.png')  # Zdjecie Ada 8.1
#img2 = cv2.imread('Crop_Img_0.png')  # Zdjecie Pawel 0

#img1 = cv2.imread('Crop_Img_8.2.png')  # Zdjecie Ada 8.2
#img2 = cv2.imread('Crop_Img_0.png')  # Zdjecie Pawel 0

#img1 = cv2.imread('Crop_Img_8.1.png')  # Zdjecie Ada 8.1
#img2 = cv2.imread('Crop_Img_1.png')  # Zdjecie Pawel 1

#img1 = cv2.imread('Crop_Img_8.2.png')  # Zdjecie Ada 8.2
#img2 = cv2.imread('Crop_Img_1.png')  # Zdjecie Pawel 1

#img1 = cv2.imread('Crop_Img_8.1.png')  # Zdjecie Ada 8.1
#img2 = cv2.imread('Crop_Img_5.1.png')  # Zdjecie Emil 5.1

#img1 = cv2.imread('Crop_Img_8.2.png')  # Zdjecie Ada 8.2
#img2 = cv2.imread('Crop_Img_5.1.png')  # Zdjecie Emil 5.1

#img1 = cv2.imread('Crop_Img_8.1.png')  # Zdjecie Ada 8.1
#img2 = cv2.imread('Crop_Img_5.2.png')  # Zdjecie Emil 5.2

#img1 = cv2.imread('Crop_Img_8.2.png')  # Zdjecie Ada 8.2
#img2 = cv2.imread('Crop_Img_5.2.png')  # Zdjecie Emil 5.2

#img1 = cv2.imread('Crop_Img_8.1.png')  # Zdjecie Ada 8.1
#img2 = cv2.imread('Crop_Img_7.1.png')  # Zdjecie Kuba 7.1

#img1 = cv2.imread('Crop_Img_8.2.png')  # Zdjecie Ada 8.2
#img2 = cv2.imread('Crop_Img_7.1.png')  # Zdjecie Kuba 7.1

#img1 = cv2.imread('Crop_Img_8.1.png')  # Zdjecie Ada 8.1
#img2 = cv2.imread('Crop_Img_7.2.png')  # Zdjecie Kuba 7.2

#img1 = cv2.imread('Crop_Img_8.2.png')  # Zdjecie Ada 8.2
#img2 = cv2.imread('Crop_Img_7.2.png')  # Zdjecie Kuba 7.2

#img1 = cv2.imread('Crop_Img_8.1.png')  # Zdjecie Ada 8.1
#img2 = cv2.imread('Crop_Img_6.1.png')  # Zdjecie Kacper 6.1

#img1 = cv2.imread('Crop_Img_8.2.png')  # Zdjecie Ada 8.2
#img2 = cv2.imread('Crop_Img_6.1.png')  # Zdjecie Kacper 6.1

#img1 = cv2.imread('Crop_Img_8.1.png')  # Zdjecie Ada 8.1
#img2 = cv2.imread('Crop_Img_6.2.png')  # Zdjecie Kacper 6.2

#img1 = cv2.imread('Crop_Img_8.2.png')  # Zdjecie Ada 8.2
#img2 = cv2.imread('Crop_Img_6.2.png')  # Zdjecie Kacper 6.2

#img1 = cv2.imread('Crop_Img_8.1.png')  # Zdjecie Ada 8.1
#img2 = cv2.imread('Crop_Img_2.1.png')  # Zdjecie Mezczyzna 2.1

#img1 = cv2.imread('Crop_Img_8.1.png')  # Zdjecie Ada 8.1
#img2 = cv2.imread('Crop_Img_2.2.png')  # Zdjecie Mezczyzna 2.2

#img1 = cv2.imread('Crop_Img_8.1.png')  # Zdjecie Ada 8.1
#img2 = cv2.imread('Crop_Img_3.png')  # Zdjecie Kobieta 3

#img1 = cv2.imread('Crop_Img_8.1.png')  # Zdjecie Ada 8.1
#img2 = cv2.imread('Crop_Img_4.png')  # Zdjecie Mezczyzna 4

#img1 = cv2.imread('Crop_Img_8.2.png')  # Zdjecie Ada 8.2
#img2 = cv2.imread('Crop_Img_2.1.png')  # Zdjecie Mezczyzna 2.1

#img1 = cv2.imread('Crop_Img_8.2.png')  # Zdjecie Ada 8.2
#img2 = cv2.imread('Crop_Img_2.2.png')  # Zdjecie Mezczyzna 2.2

#img1 = cv2.imread('Crop_Img_8.2.png')  # Zdjecie Ada 8.2
#img2 = cv2.imread('Crop_Img_3.png')  # Zdjecie Kobieta 3

#img1 = cv2.imread('Crop_Img_8.2.png')  # Zdjecie Ada 8.2
#img2 = cv2.imread('Crop_Img_4.png')  # Zdjecie Mezczyzna 4


img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# sift
sift = cv2.xfeatures2d.SIFT_create()

keypoints_1, descriptors_1 = sift.detectAndCompute(img1, None)
keypoints_2, descriptors_2 = sift.detectAndCompute(img2, None)

# feature matching
bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

matches = bf.match(descriptors_1, descriptors_2)

matches = sorted(matches, key=lambda x: x.distance)
print("Liczba punktów wspólnych:", len(list(matches)))

img3 = cv2.drawMatches(img1, keypoints_1, img2,
                       keypoints_2, matches[:50], img2, flags=2)
plt.imshow(img3), plt.show()
