import cv2

# Get the IP address and port number of your phone
ip_address = "192.168.1.3"
port_number = 8080

# Create a VideoCapture object using the IP address and port number of your phone
cap = cv2.VideoCapture(f"http://{ip_address}:{port_number}/video")

# Create a loop to capture frames from your phone's camera
while True:
    # Capture a frame from your phone's camera
    ret, frame = cap.read()

    # Check if the frame was successfully captured
    if ret:
        # Display the frame on a screen
        cv2.imshow("Phone Camera", frame)

        # Wait for a key to be pressed
        key = cv2.waitKey(1)

        # If the 'q' key is pressed, break out of the loop
        if key == ord("q"):
            break

    # Close the VideoCapture object
    cap.release()
