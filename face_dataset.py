import cv2
import os 

cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# For each person, enter one numeric face id
face_id = input('\n Enter user id and press <return> ==>  ')
print('\n [INFO] Initializing face capture. Look at the camera and wait ...')

# Initialize individual sampling face count
count = 0
while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray, 
        scaleFactor=1.3, 
        minNeighbors=5
        )
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        count += 1
        # Save the captured image into the datasets folder
        cv2.imwrite("facialRecognitionProject/dataset/User." + str(face_id) + "." + str(count) + ".jpg", gray[y:y+h, x:x+w])
        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff
    if k == 27:
        break
    elif count >= 30:
        break

print('\n [INFO] Exiting program and cleaning up data')
cam.release()
cv2.destroyAllWindows()
