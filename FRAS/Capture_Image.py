import csv
import cv2
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False

def takeImages():
    root = tk.Tk()
    root.withdraw()
    
    Id = simpledialog.askstring("Input", "Enter Your ID:")
    name = simpledialog.askstring("Input", "Enter Your Name:")
    
    if Id and name and is_number(Id) and name.isalpha():
        cam = cv2.VideoCapture(0)
        # Load Haar cascade and check if loaded properly
        detector = cv2.CascadeClassifier(r"D:\Face-Recognition-Attendance-System-master\FRAS\haarcascade_frontalface_default.xml")
        if detector.empty():
            messagebox.showerror("Error", "Error loading Haar cascade file!")
            return

        sampleNum = 0
        
        while True:
            ret, img = cam.read()
            if not ret:
                messagebox.showerror("Error", "Failed to capture image from camera.")
                break

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
           
            faces = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            for x, y, w, h in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (10, 159, 255), 2)
                sampleNum += 1
                # Ensure TrainingImage folder exists
                os.makedirs("TrainingImage", exist_ok=True)
                cv2.imwrite(f"TrainingImage/{name}.{Id}.{sampleNum}.jpg", gray[y:y+h, x:x+w])
                cv2.imshow('Face Capture', img)

            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            elif sampleNum >= 100:
                break
        
        cam.release()
        cv2.destroyAllWindows()
        
        messagebox.showinfo("Success", f"Images Saved for ID: {Id}, Name: {name}")
        
        # Ensure StudentDetails folder exists
        os.makedirs("StudentDetails", exist_ok=True)

        csv_file = "StudentDetails/StudentDetails.csv"
        header = ["Id", "Name"]
        row = [Id, name]
        
        if os.path.isfile(csv_file):
            with open(csv_file, 'a+', newline='') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)
        else:
            with open(csv_file, 'w', newline='') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(header)
                writer.writerow(row)
    else:
        if not is_number(Id):
            messagebox.showerror("Error", "Enter Numeric ID")
        if not name.isalpha():
            messagebox.showerror("Error", "Enter Alphabetical Name")
