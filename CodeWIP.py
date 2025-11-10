# import the OpenCV library - it's called cv2
import cv2
# load the Haar Cascade algorithm from the XML file into OpenCV
alg = "haarcascade_frontalface_default.xml" #Replace with the appropriate path
haar_cascade = cv2.CascadeClassifier(alg)
# read the image as grayscale
file_name = '<INSERT YOUR IMAGE NAME HERE>' #copy path and place here
img = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
# find the faces in that image
# this gives back an array of face locations and sizes
faces = haar_cascade.detectMultiScale(
    gray_img,
    scaleFactor=1.05,
    minNeighbors=2,
    minSize=(100, 100)
)
# for each face detected
for x, y, w, h in faces:
    # crop the image to select only the face
    cropped_image = img[y : y + h, x : x + w]
    # write the cropped image to a file
    target_file_name = '<INSERT YOUR TARGET IMAGE NAME HERE>'
    cv2.imwrite(
        target_file_name,
        cropped_image,
    )
