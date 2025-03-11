import yagmail
import os
import datetime

# Ensure 'Attendance' directory exists
path = 'Attendance'
if not os.path.exists(path):
    print("Error: 'Attendance' directory not found!")
    exit()

# Get the latest attendance file
files = sorted(os.listdir(path), key=lambda x: os.path.getmtime(os.path.join(path, x)))
if not files:
    print("Error: No files found in 'Attendance' folder.")
    exit()

newest = files[-1]  # Latest file
file_path = os.path.join(path, newest)

# Email details
receiver = "24522705.acs@dypvp.edu.in"
sub = "Attendance Report for " + datetime.date.today().strftime("%B %d, %Y")
body = "Please find the attached attendance logs."

# Secure email credentials
EMAIL_USER = "tejasph1@gmail.com"
EMAIL_PASS = "hrbq altz qvcj hgdi"  # Use App Password

# Send email using yagmail
try:
    yag = yagmail.SMTP(EMAIL_USER, EMAIL_PASS)
    yag.send(
        to=receiver,
        subject=sub,
        contents=body,
        attachments=file_path
    )
    print("✅ Email Sent Successfully!")
except Exception as e:
    print(f"❌ Error sending email: {e}")
