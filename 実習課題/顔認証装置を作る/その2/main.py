import face_recognition
import cv2
import numpy as np
video_capture = cv2.VideoCapture(0)
obama_image = face_recognition.load_image_file("/home/pi/python/実習課題/顔認証装置を作る/その2/biden.jpg")

obama_face_encoding = face_recognition.face_encodings(obama_image)[0] 
biden_image = face_recognition.load_image_file("/home/pi/python/実習課題/顔認証装置を作る/その2/obama.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0] 
known_face_encodings = [
    obama_face_encoding,
    biden_face_encoding
]
known_face_names = [
    "Barack Obama",
    "Joe Biden"
]
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
while True:
    ret, frame = video_capture.read()
    if process_this_frame:
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        face_locations = face_recognition.face_locations(small_frame)
        face_encodings = face_recognition.face_encodings(small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            face_names.append(name)
    process_this_frame = not process_this_frame
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 125, 255), 5)
        font = cv2.FONT_HERSHEY_TRIPLEX 
        cv2.putText(frame, name, (left + 10, bottom + 35), font, 1.0, (0, 0, 255), 1)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()