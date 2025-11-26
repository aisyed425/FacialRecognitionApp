import cv2

# load the Haar Cascade algorithm from the XML file into OpenCV
alg = "haarcascade_frontalface_default.xml"  Replace with the appropriate path
haar_cascade = cv2.CascadeClassifier(alg)

# read the image as grayscale
file_name = '<INSERT YOUR IMAGE NAME HERE>'  # Copy full path and place here
img = cv2.imread(file_name, 0)
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# find the faces in that image
# this gives back an array of face locations and sizes
faces = haar_cascade.detectMultiScale(
    gray_img,
    scaleFactor=1.05,
    minNeighbors=2,
    minSize=(100, 100)
)
i = 0
# for each face detected
for x, y, w, h in faces:
    # crop the image to select only the face
    cropped_image = img[y : y + h, x : x + w]

    # write the cropped image to a file
    target_file_name = 'stored_faces/' + str(i) + '.jpg'  # You can change folder name if needed
    cv2.imwrite(
        target_file_name,
        cropped_image,
    )
    i += 1


#Minor Brainstorm:
# How do I make this work for a door lock?
#How do I make the door lock?
# May need tinkercad or another CAD software to design the lock/mechanise/simulation
