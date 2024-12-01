from ultralytics import YOLO
import cv2

# Load a COCO-pretrained YOLO model
model = YOLO("yolo11n.pt")

# Define vehicle class IDs and their labels (from COCO dataset)
VEHICLE_CLASSES = {2: "Car", 3: "Motorcycle", 5: "Bus", 7: "Truck", 9: "Rickshaw"}

# Initialize vehicle counters
car_count = 0
motorcycle_count = 0
bus_count = 0
truck_count = 0

image_source = "D:/Project/vehicle_images/trafficphoto4"

# Define a function to detect vehicles
def detect_vehicles(frame, threshold=0.3, iou_threshold=0.3):
    results = model(frame, conf=threshold, iou=iou_threshold)  # Set confidence threshold here
    detections = results[0].boxes.data  # Get the detected boxes

    for det in detections:
        x1, y1, x2, y2, conf, cls = det
        if conf < threshold:  # Skip detections below the threshold
            continue

        label = results[0].names[int(cls)]  # Map class index to label

        # Draw rectangle and label on the image
        frame = cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        frame = cv2.putText(frame, f"{label} {conf:.2f}", (int(x1), int(y1) - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return frame


def detect_vehicles_in_image(image_path):
    global car_count, motorcycle_count, bus_count, truck_count

    # Load image
    frame = cv2.imread(image_path)
    if frame is None:
        print("Error: Could not load image.")
        return

    # Run vehicle detection
    results = model(frame)  # Perform detection
    detections = results[0].boxes.data  # Access detected boxes

    # Iterate over detections and draw on the image
    for det in detections:
        x1, y1, x2, y2, conf, cls = det.tolist()  # Convert tensor to list
        if conf < 0.3:  # Confidence threshold
            continue

        class_id = int(cls)
        label = VEHICLE_CLASSES.get(class_id, "Unknown")  # Map class ID to label
        if label in VEHICLE_CLASSES.values():  # Only process vehicle classes
            # Increment counters for each vehicle type
            if label == "Car":
                car_count += 1
            elif label == "Motorcycle":
                motorcycle_count += 1
            elif label == "Bus":
                bus_count += 1
            elif label == "Truck":
                truck_count += 1

            frame = cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            frame = cv2.putText(frame, f"{label} {conf:.2f}", (int(x1), int(y1) - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Show the image with vehicle detection
    cv2.imshow("Vehicle Detection", frame)

    # Save the result image
    cv2.imwrite(f"{image_source}_result.jpg", frame)

    # Write vehicle counts to a file
    with open("vehicle_count.txt", "w") as file:
        file.write(f"Cars: {car_count}\n")
        file.write(f"Motorcycles: {motorcycle_count}\n")
        file.write(f"Buses: {bus_count}\n")
        file.write(f"Trucks: {truck_count}\n")

    # Print the vehicle counts
    print(f"Cars: {car_count}")
    print(f"Motorcycles: {motorcycle_count}")
    print(f"Buses: {bus_count}")
    print(f"Trucks: {truck_count}")

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Run the detection on a single image
    detect_vehicles_in_image(image_source + ".jpg")