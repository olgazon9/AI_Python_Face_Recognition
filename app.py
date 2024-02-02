import cv2
from tkinter import *
from tkinter import simpledialog
import os
import xml.etree.ElementTree as ET
from PIL import Image, ImageTk

# Initialize the face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Directory to save user images
user_images_directory = "user_images"
if not os.path.exists(user_images_directory):
    os.makedirs(user_images_directory)

# Function to capture video from webcam and detect faces
def video_stream():
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, video_stream)

# Save user data to XML
def save_user_to_xml(name, image_file):
    xml_file = os.path.join(user_images_directory, "users.xml")
    if not os.path.exists(xml_file):
        root = ET.Element("users")
    else:
        tree = ET.parse(xml_file)
        root = tree.getroot()

    # Check if user already exists
    exists = root.findall(f"./user[@name='{name}']")
    if not exists:
        user = ET.SubElement(root, "user")
        user.set("name", name)
        user.text = image_file
        tree = ET.ElementTree(root)
        tree.write(xml_file)
        update_status(f"User {name} registered.")
    else:
        update_status(f"User {name} already registered.")

# Find user by image file name in XML
def find_user_by_image(image_file):
    xml_file = os.path.join(user_images_directory, "users.xml")
    if os.path.exists(xml_file):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for user in root.findall("user"):
            if user.text == image_file:
                return user.get("name")
    return None

# Register a new user
def register_user():
    name = simpledialog.askstring("Input", "What is your name?", parent=root)
    if name:
        ret, frame = cap.read()
        if ret:
            image_file = f"{name}.jpg"
            cv2.imwrite(os.path.join(user_images_directory, image_file), frame)
            save_user_to_xml(name, image_file)

# Recognize user (simulation)
def recognize_user():
    files = os.listdir(user_images_directory)
    if "users.xml" in files:
        files.remove("users.xml")  # Exclude the XML file from the list
    if files:
        latest_image_file = max([os.path.join(user_images_directory, f) for f in files], key=os.path.getctime)
        latest_image_name = os.path.basename(latest_image_file)
        user_name = find_user_by_image(latest_image_name)
        if user_name:
            update_status(f"Recognized User: {user_name}")
        else:
            update_status("User not recognized.")
    else:
        update_status("No users registered.")

# Update status label with message
def update_status(message):
    status_label.config(text=message)

# Main GUI application setup
root = Tk()
root.bind('<Escape>', lambda e: root.quit())
lmain = Label(root)
lmain.pack()

# Status label for displaying messages
status_label = Label(root, text="Welcome!", fg="blue")
status_label.pack()

# Button for user registration
register_btn = Button(root, text="Register User", command=register_user)
register_btn.pack()

# Button for user recognition
recognize_btn = Button(root, text="Recognize User", command=recognize_user)
recognize_btn.pack()

# Initialize webcam
cap = cv2.VideoCapture(0)
video_stream()

root.mainloop()
