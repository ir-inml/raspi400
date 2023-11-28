import cv2
img = cv2.imread("/home/pi/python/python基礎構文を使った演習/演習【その2】画像処理とOpenCVライブラリ/input.jpg")
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("/home/pi/python/python基礎構文を使った演習/演習【その2】画像処理とOpenCVライブラリ/output.jpg",imgray)