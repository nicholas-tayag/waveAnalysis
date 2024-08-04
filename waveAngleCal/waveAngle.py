import cv2
import numpy as np
import math
import os

# Paths to the images
image_paths = [
    r"waveAngleCal\imgs\pic1.png",
    r"waveAngleCal\imgs\pic2.png"
]

def process_image(image_path):
    if not os.path.exists(image_path):
        print(f"Error: The file at path '{image_path}' does not exist.")
        return

    img = cv2.imread(image_path)
    
    if img is None:
        print(f"Error: Failed to load image from '{image_path}'. Please check the file path and integrity.")
        return

    # Resize the image to a smaller size for display
    height, width = img.shape[:2]
    max_height = 800  # Maximum height of the window
    max_width = 800   # Maximum width of the window

    # Calculate the scale ratio while maintaining aspect ratio
    scale = min(max_width / width, max_height / height)

    # Resize the image
    resized_img = cv2.resize(img, (int(width * scale), int(height * scale)))

    # Store points clicked
    points = []

    # Mouse callback function to get the coordinates
    def click_event(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN and len(points) < 3:
            # Convert the coordinates back to the original image scale
            original_x = int(x / scale)
            original_y = int(y / scale)
            points.append((original_x, original_y))

            # Draw a circle at the point
            cv2.circle(resized_img, (x, y), 5, (0, 255, 0), -1)
            # Put the text of the coordinates near the point
            text = f"({original_x}, {original_y})"
            cv2.putText(resized_img, text, (x + 10, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            cv2.imshow('image', resized_img)

            # If three points have been clicked, calculate the angle and show result
            if len(points) == 3:
                x1, y1 = points[0]
                x2, y2 = points[-1]
                angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
                print(f"Break angle for {os.path.basename(image_path)}: {angle:.2f} degrees")
                # After displaying the angle, wait for a key press and close the window
                cv2.waitKey(0)
                cv2.destroyAllWindows()

    # Display the resized image and set the mouse callback
    cv2.imshow('image', resized_img)
    cv2.setMouseCallback('image', click_event)

    # Wait for a key to exit
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Process each image
for path in image_paths:
    process_image(path)
