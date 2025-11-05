# I will add stage one of my code here.
# Screenshots 
import cv2

# Load the built-in face detector (Haar Cascade)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Start video capture (0 = default webcam, or use your Pi camera)
cap = cv2.VideoCapture(0)
