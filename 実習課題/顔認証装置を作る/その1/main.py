import cv2
cap = cv2.VideoCapture(0)
cascade_path = "/home/pi/python/実習課題/顔認証装置を作る/その1/haarcascade_frontalface_default.xml"
facecascade = cv2.CascadeClassifier(cascade_path)
while cap.isOpened():
    red,frame = cap.read()
    if red:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = facecascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=10,minSize=(10,10),maxSize=(300,300))
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,125,255),10)
        cv2.imshow('カメラ',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.relese()
cv2.destroyAllWindows()