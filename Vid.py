import cv2

capture = cv2.VideoCapture(0)
face_hear_cascade = cv2. CascadeClassifier('haarcascade_frontalface')
while True:
    _, image = capture.read()
    gray = cv2.cvColor(image, cv2.COLOR_BGR2GRAY)
    face = face_hear_cascade.detectMultiScale(gray, 1,1,4)

    for(x,y,w,h) in faces:
        cv2.rectangle(image,(x,y), (x+w, y+h),
                      (0, 255, 0), 5)
        cv2.imshow('Video', image)
        k = cv2.waitkey(30) & 0xFF
        if k==27:
            break

cv2.release()