import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import check_camera
import Capture_Image
import Train_Image
import Recognize
from threading import Thread

# Function to check the camera
def checkCamera():
    check_camera.camer()
    messagebox.showinfo("Info", "Camera check complete. Returning to main menu.")

# Function to capture faces
def CaptureFaces():
    Capture_Image.takeImages()
    messagebox.showinfo("Info", "Face capture complete. Returning to main menu.")

# Function to train images
def Trainimages():
    Train_Image.TrainImages()
    messagebox.showinfo("Info", "Training images complete. Returning to main menu.")

# Function to recognize faces and attendance
def recognizeFaces():
    Recognize.recognize_attendance()
    messagebox.showinfo("Info", "Face recognition and attendance complete. Returning to main menu.")

# Function to send auto mail
def sendAutoMail():
    os.system("py automail.py")
    messagebox.showinfo("Info", "Auto mail sent. Returning to main menu.")

# Function to create a card with an image, text, and a button
def create_card(frame, image_path, text, command):
    card_frame = tk.Frame(frame, bd=2, relief=tk.RAISED, padx=10, pady=10)
    img = Image.open(os.path.join(r"D:\Face-Recognition-Attendance-System-master\img", image_path))
    img = img.resize((140, 150))
    img = ImageTk.PhotoImage(img)
    label_img = tk.Label(card_frame, image=img)
    label_img.image = img  # Keep reference
    label_img.pack()

    label_text = tk.Label(card_frame, text=text, font=("Arial", 12, "bold"))
    label_text.pack()

    button = tk.Button(card_frame, text="Select", command=command, bg="#007BFF", fg="white")
    button.pack()

    card_frame.pack(side=tk.LEFT, padx=10, pady=10)

# Main GUI application
def mainGUI():
    root = tk.Tk()
    root.title("Face Recognition Attendance System")
    root.geometry("1080x720")

    title_label = tk.Label(root, text="Face Recognition Attendance System", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    frame = tk.Frame(root)
    frame.pack()

    create_card(frame, "check.png", "Check Camera", checkCamera)
    create_card(frame, "capture.png", "Capture Faces", CaptureFaces)
    create_card(frame, "train.png", "Train Images", Trainimages)
    create_card(frame, "recognize.png", "Recognize", recognizeFaces)
    create_card(frame, "mail.png", "Auto Mail", sendAutoMail)

    quit_button = tk.Button(root, text="Quit", command=root.quit, bg="red", fg="white", font=("Arial", 12, "bold"))
    quit_button.pack(pady=10)

    root.mainloop()

# Main driver
if __name__ == "__main__":
    mainGUI()