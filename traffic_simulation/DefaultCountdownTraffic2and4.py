def load_vehicle_counts(file_path):
    # initialize the vehicle counts
    global car_count
    global bus_count
    global truck_count
    try:
        # Read the file
        with open(file_path, "r") as file:
            for line in file:
                # Split the line into label and count
                label, count = line.strip().split(":")
                count = int(count.strip())  # Convert count to integer

                # Assign counts to variables based on the label
                if label == "Cars":
                    car_count = count
                elif label == "Motorcycles":
                    pass
                elif label == "Buses":
                    bus_count = count
                elif label == "Trucks":
                    truck_count = count
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except ValueError:
        print("Error: File content is not in the expected format.")

    return car_count, bus_count, truck_count

car_count, bus_count, truck_count = load_vehicle_counts("D:/Project/vehicle_count.txt")

# Default countdown number
green_traffic_up_right_countdown = 6
green_traffic_left_countdown = 4
yellow_traffic_countdown = 5
red_traffic_countdown = green_traffic_up_right_countdown + green_traffic_left_countdown + yellow_traffic_countdown

def adjust_traffic_light(number_of_car, number_of_bus, number_of_truck):
    """
    Adjusts the red traffic light countdown based on detected vehicles.
    """
    global green_traffic_up_right_countdown
    global green_traffic_left_countdown
    global red_traffic_countdown

    # if vehicles are more than 20
    if number_of_car + number_of_bus + number_of_truck > 14:
        green_traffic_up_right_countdown += 15 # increment forward and right traffic light by 15 seconds
        green_traffic_left_countdown += 10 # increment left traffic light by 10 seconds

    red_traffic_countdown = green_traffic_up_right_countdown + green_traffic_left_countdown + yellow_traffic_countdown

    # Return updated countdowns
    return green_traffic_up_right_countdown, green_traffic_left_countdown, red_traffic_countdown

# Adjust traffic light countdown
green_traffic_up_right_countdown, green_traffic_left_countdown, red_traffic_countdown = adjust_traffic_light(car_count, bus_count, truck_count)
