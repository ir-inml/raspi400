import cv2
cap = cv2.VideoCapture(0)
red,frame = cap.read()
if red:
    cv2.imwrite('test.jpg',frame)
cap.release()