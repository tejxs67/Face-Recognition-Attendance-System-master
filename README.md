

# 🧠 Face Recognition Attendance System

A complete **Face Recognition Attendance System** built with **Python**, powered by **OpenCV**, **LBPH algorithm**, and **Haar Cascades**.  
Automates student attendance with real-time facial recognition, secured CSV logging, and auto-email notifications.

---

## 🔧 Built With

- **Python 3.7**

---

## 📦 Modules Used

_All modules are used with their latest stable versions:_

- [OpenCV (Contrib 4.0.1)](https://docs.opencv.org/3.4/index.html)
- [Pillow](https://pypi.org/project/Pillow/)
- [NumPy](https://numpy.org/)
- [Pandas](https://pandas.pydata.org/)
- [Shutil](https://docs.python.org/3/library/shutil.html)
- [CSV](https://docs.python.org/3/library/csv.html)
- [Yagmail](https://pypi.org/project/yagmail/)

---

## 🧠 Face Recognition Algorithms

- [Haar Cascade Classifier](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html)
- [LBPH (Local Binary Pattern Histogram)](https://docs.opencv.org/3.4/da/d60/tutorial_face_main.html)

---

## 💻 Software Used

- [PyCharm 2019.2](https://www.jetbrains.com/pycharm/download/?section=windows)
- [VS Code](https://code.visualstudio.com/download)
- [Git](https://git-scm.com/downloads)

---

## 🔑 Installation Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/face-recognition-attendance.git
```
Or [Download ZIP](https://github.com/kmhmubin/Face-Recognition-Attendance-System/archive/refs/heads/master.zip) and extract.

### 2️⃣ Create Python Virtual Environment

```bash
python -m venv env
```

### 3️⃣ Activate Environment (Windows)

```bash
.\env\Scripts\activate
```

> 📌 If you don't have `venv` or `pip`, follow [this guide](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

### 4️⃣ Install Required Packages

```bash
pip install opencv-contrib-python
pip install numpy
pip install pandas
pip install Pillow
pip install pytest-shutil
pip install python-csv
pip install yagmail
```

---

## 🧪 Run the System

```bash
py main.py
```

> Make sure your webcam is connected. The app launches a GUI with buttons to:  
> - Check camera  
> - Capture face data  
> - Train recognizer  
> - Recognize faces  
> - Mark attendance  
> - Send email notifications  

---

## 📝 How to Use

1. Clone the project
2. Open in your preferred IDE (PyCharm / VSCode)
3. Create virtual environment
4. Install all dependencies
5. Configure sender email in the script (Yagmail)
6. Run `main.py`
7. Use GUI to capture, train, recognize, and log attendance

---

## 📩 Email Integration

Make sure to update sender credentials in the script before using the **Send Mail** function. Uses **Yagmail** for simplified SMTP.

---
