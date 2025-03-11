import cv2

# Load cascade
face_cascade = cv2.CascadeClassifier(r"D:\Face-Recognition-Attendance-System-master\FRAS\haarcascade_frontalface_default.xml")

if face_cascade.empty():
    print("Error: Cascade file could not be loaded!")
    exit()

# Start webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot open webcam!")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame!")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the grayscale image
    cv2.imshow("Gray Image", gray)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4, minSize=(30, 30))

    if len(faces) == 0:
        print("No faces detected!")
    else:
        print(f"{len(faces)} faces detected.")

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
