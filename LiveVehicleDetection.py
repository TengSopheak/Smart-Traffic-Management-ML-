import cv2
from ultralytics import YOLO

# Load the YOLOv8/YOLOv11 model
model = YOLO("yolo11n.pt")

# Define a function to detect vehicles
def detect_vehicles(frame, threshold=0.3):
    results = model(frame, conf=threshold)  # Set confidence threshold here
    detections = results[0].boxes.data  # Get the detected boxes
    for det in detections:
        x1, y1, x2, y2, conf, cls = det
        if conf < threshold:  # Skip detections below the threshold
            continue
        label = results[0].names[int(cls)]  # Map class index to label
        # Add "motorcycle" to the list of vehicle labels
        if label in ["car", "bus", "bike", "truck", "rickshaw", "motorcycle"]:
            # Draw rectangle and label
            frame = cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            frame = cv2.putText(frame, f"{label} {conf:.2f}", (int(x1), int(y1) - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return frame

# Capture live video feed from webcam
cap = cv2.VideoCapture("video/TrafficViewPhnomPenh.mp4")  # Use `0` for default webcam or path to a video file.

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame. Exiting...")
        break

    # Detect vehicles in the frame with a threshold of 0.3
    frame = detect_vehicles(frame, threshold=0.3)

    # Display the frame with detections
    cv2.imshow("Live Vehicle Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # 27 is the ASCII code for the 'Esc' key
        print("Exiting...")
        break

# Release the video capture and close windows
cap.release()
cv2.destroyAllWindows()
