# Virtual Mouse using OpenCV

## Project Overview
This project implements a virtual mouse using OpenCV, a computer vision library. It allows users to control their computer cursor using hand gestures captured by a webcam. By leveraging advanced image processing techniques, the system detects and tracks the user's hand movements in real-time, enabling intuitive and hands-free control of the mouse pointer.

## Features
- **Hand Detection:** Utilizes the Mediapipe library for accurate hand detection and landmark tracking.
- **Gesture Recognition:** Recognizes predefined hand gestures to perform mouse actions such as clicking and dragging.
- **Real-time Tracking:** Achieves smooth and responsive tracking of hand movements for seamless cursor control.
- **User-Friendly Interface:** Provides a simple and intuitive interface for users to interact with the virtual mouse using their hands.
- **Customizable Gestures:** Allows users to define custom gestures for specific mouse actions, enhancing personalization and usability.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/virtual-mouse.git
    ```
2. Navigate to the project directory:
    ```bash
    cd virtual-mouse
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Ensure you have a webcam connected to your computer.
2. Run the main script:
    ```bash
    python main.py
    ```
3. Position your hand in front of the webcam, and the virtual mouse will track your hand movements.
4. Perform gestures to control the cursor:
   - **Click:** Close your hand into a fist.
   - **Drag:** Extend your index and middle fingers while keeping others closed.
   - **Scroll:** Tilt your hand up or down.
   - *(Custom gestures can be defined as per user preferences.)*
5. Press `Esc` to exit the application.

## Demo
Include a GIF or video demonstrating the virtual mouse in action.

## Dependencies
- Python 3.x
- OpenCV
- Mediapipe

## Contributing
Contributions are welcome! Please follow the [Contribution Guidelines](CONTRIBUTING.md).

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgements
- [Mediapipe](https://google.github.io/mediapipe/)
- [OpenCV](https://opencv.org/)
