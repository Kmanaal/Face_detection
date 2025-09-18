import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.SerialModule import SerialObject

cap = cv2.VideoCapture(0)
detector = FaceDetector()
arduino = SerialObject('COM4')

def make_1080p():
    cap.set(3, 1920)
    cap.set(4, 1080)

def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)

def make_480p():
    cap.set(3, 640)
    cap.set(4, 480)

def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)

make_1080p()
change_res(300, 100)


while True:
    success, img = cap.read()

    img, bBoxes = detector.findFaces(img)
    if bBoxes:
        arduino.sendData([1,0])
    else:
        arduino.sendData([0,1])

    cv2.imshow("Video", img)
    cv2.waitKey(1)
