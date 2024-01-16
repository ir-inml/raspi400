import cv2
cap = cv2.VideoCapture(0)
while cap.isOpened():
    red,frame = cap.read()
    cv2.imshow('カメラ',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.relese()
cv2.destroyAllWindows()