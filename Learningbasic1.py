import cv2
import sys
import numpy as np
import winsound

cascPath = sys.argv[0]

faceDetector = cv2.CascadeClassifier('C:\\Users\BungK\OneDrive\Documents\opencv-4.2.0\data\haarcascades\haarcascade_frontalface_default.xml')

videocapture = cv2.VideoCapture(0)

def PLAYSOUND():
    FN = r'C:\\Users\BungK\source\repos\Learningbasic1\Sound\AlarnEditor.wav'
    winsound.PlaySound(FN, winsound.SND_FILENAME)

def STOPSOUND():
    StopSound = ('Stop Alarn and Start Security Again')
    inputcommand_StopAlarn = str('Please input Command to stopAlarn : ')
    for inputcommand_StopAlarn in StopSound:
        winsound.PlaySound(None, winsound.SND_PURGE)
    


while True:
    # Capture frame-by-frame
    ret, frame = videocapture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    faces = faceDetector.detectMultiScale(gray, 1.3, 5, 2)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        PLAYSOUND()

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()