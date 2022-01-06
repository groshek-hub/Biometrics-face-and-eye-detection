import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# cv2.namedWindow("Face and Eye Detection + image capture")
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml')

img_counter = 0


def detect():
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)
        roi_gray = gray[y:y+w, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.2, 5)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey),
                          (ex + ew, ey + eh), (255, 0, 0), 5)


while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    detect()

    k = cv2.waitKey(1)
    if k % 256 == 32:
        detect()
        # SPACE pressed
        print("SPACE hit, capture image to .png")
        img_name = "Img_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

    cv2.imshow('Face and Eye detection program', frame)

    if k % 256 == 27:
        # ESC pressed
        print("ESC hit, closing program")
        break

cap.release()
cv2.destroyAllWindows()
