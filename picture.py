import cv2

face_haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image = cv2.imread('face_pic.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)




faces = face_haar_cascade.detectMultiScale(gray, 1.1, 4)


for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 225,0), 5
                  )
    cv2.imshow("faces", image)
    cv2.waitKey()