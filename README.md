# AI Python Face Recognition

## Project Explanation

This AI Python Face Recognition project is designed to introduce users to the basics of face recognition technology using Python. By leveraging the powerful OpenCV library for face detection and the Tkinter library for building a graphical user interface (GUI), this project allows users to register their faces into the system and then recognize them through a simple GUI.

The core functionality revolves around the use of a webcam to capture live video feed, detect faces within that feed, and perform operations such as registering and recognizing faces. The project simplifies the complex field of face recognition into an approachable example for beginners and enthusiasts alike, showcasing how Python can be used to interact with hardware devices like webcams and implement real-world applications.

### Features

- **User Registration**: Users can register their faces with the system, which captures and stores their images.
- **Face Recognition**: The system can recognize registered users by matching their current image from the webcam feed against the stored images.
- **XML Data Handling**: User data is managed using XML files, making it easier to store and retrieve user information efficiently.
- **GUI**: A user-friendly graphical interface allows for easy interaction with the system, making it accessible to users with varying levels of technical expertise.

## Usage Instructions

### Getting Started

To use this face recognition system, follow the steps outlined below. These instructions will guide you from setting up your environment to running the application.

#### Prerequisites

Ensure you have the following installed on your system:

- Python 3.x
- OpenCV library
- Pillow library
- lxml library

#### Installation

1. Clone the project repository to your local machine using:

    ```bash
    git clone https://github.com/olgazon9/AI_Python_Face_Recognition.git
    ```

2. Navigate to the project directory:

    ```bash
    cd AI_Python_Face_Recognition
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    Alternatively, install each library individually:

    ```bash
    pip install opencv-python-headless Pillow lxml
    ```

### Running the Application

Execute the following command in the project directory to start the application:

```bash
python app.py
