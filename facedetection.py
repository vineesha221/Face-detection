import cv2
path = (r'C:\Users\vineesha thoutam\Downloads\b.jpg')
image = cv2.imread(path)
window_name = 'vinisha'
height, width, channels = image.shape
print (height, width, channels)
image = cv2.resize(image, (600,600))
cv2.imshow(window_name, image)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", gray_image)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
detected_faces = face_cascade.detectMultiScale(image, scaleFactor=1.3, minNeighbors=1)
for x, y, w, h in detected_faces:
    cv2.rectangle(image, (x,y), (x+w, y+h), (0, 0, 255), thickness=2)
cv2.imshow("Face Detect", image)
cv2.waitKey(0)