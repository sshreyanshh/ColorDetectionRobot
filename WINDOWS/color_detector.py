import cv2
import socket

# WSL IP address
WSL_IP = "172.30.104.20"
PORT = 5000

# Connect to the ROS 2 bridge
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((WSL_IP, PORT))

print("Connected to ROS 2 color bridge.")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera could not be opened.")
    client.close()
    exit()

print("Color Detector started. Press Q to quit.")

last_color = ""

while True:
    ret, frame = cap.read()

    if not ret:
        print("Could not read camera frame.")
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    red_lower = (0, 100, 100)
    red_upper = (10, 255, 255)

    green_lower = (40, 50, 50)
    green_upper = (80, 255, 255)

    blue_lower = (100, 100, 100)
    blue_upper = (140, 255, 255)

    red_mask = cv2.inRange(hsv, red_lower, red_upper)
    green_mask = cv2.inRange(hsv, green_lower, green_upper)
    blue_mask = cv2.inRange(hsv, blue_lower, blue_upper)

    red_pixels = cv2.countNonZero(red_mask)
    green_pixels = cv2.countNonZero(green_mask)
    blue_pixels = cv2.countNonZero(blue_mask)

    if red_pixels > green_pixels and red_pixels > blue_pixels and red_pixels > 500:
        detected_color = "RED"
    elif green_pixels > red_pixels and green_pixels > blue_pixels and green_pixels > 500:
        detected_color = "GREEN"
    elif blue_pixels > red_pixels and blue_pixels > green_pixels and blue_pixels > 500:
        detected_color = "BLUE"
    else:
        detected_color = "NO COLOR"

    # Send the color only when it changes
    if detected_color != last_color:
        client.sendall((detected_color + "\n").encode())
        print("Sent:", detected_color)
        last_color = detected_color

    cv2.putText(
        frame,
        "Detected: " + detected_color,
        (30, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2
    )

    cv2.imshow("Color Detective Robot", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
client.close()
cv2.destroyAllWindows()
