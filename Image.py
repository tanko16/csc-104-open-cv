import cv2

face_hear_cascade = cv2.CaescadeClassifier('hearcascade_frontalface_')
image - cv2.imread('demo.jpg')
gray = cv2.cvtcolor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Gray',gray)
#cv2.waitkey()


faces = cface_hear_cascade.detcteMultiScale(gray, 1,1,4)

for(x,y,w,h) in faces:
    cv2.rectangle(image,(x,y), (x+w, y+h),
                  (0,255,0), 5)
cv2.imshow('Faces', image)
cv2.waitKey()
