# OpenCV program to detect face in real time
# import libraries of python OpenCV
# where its functionality resides
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
eye_Glass = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

# capture frames from a camera
img=cv2.imread('m2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# convert to gray scale of each frames
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # Detects faces of different sizes in the input image
for (x,y,w,h) in faces:
     # To draw a rectangle in a face
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    # Detects eyes of different sizes in the input image
    eyes = eye_cascade.detectMultiScale(roi_gray)
    # Detects eyes of different sizes in the input image
    for (ex,ey,ew,eh) in eyes:
        #To draw a rectangle in eyes
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)
# Display an image in a window
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
