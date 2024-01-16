import cv2
import time
cap = cv2.VideoCapture(0)
fmt = cv2.VideoWriter_fourcc(*"XVID")
fps = 20.0
size = (640,480)
writer = cv2.VideoWriter("video.avi",fmt,fps,size)
start = time.time()
while True:
    red,frame = cap.read()
    if not red:
        break
    resize_frame = cv2.resize(frame,size)
    writer.write(resize_frame)
    cv2.imshow("カメラ",resize_frame)
    now = time.time()
    if cv2.waitKey(1) == 27 or now > start+7:
        break
writer.release()
cap.release()
cv2.destroyAllWindows()