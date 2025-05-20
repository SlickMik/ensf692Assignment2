# input_processing.py
# <Ibrahim Khan>, ENSF 692 Spring 2025
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.



# No global variables are permitted
# Sensor class to store and update sensor status
class Sensor:
    # Constructor with default values
    def __init__(self, light = "red", pedestrian = "no", vehicle = "no"):
        self.light = light
        self.pedestrian = pedestrian
        self.vehicle = vehicle

    # Update sensor status if new values are provided
    def update_status(self, light = None, pedestrian = None, vehicle = None):
        if light is not None:
            self.light = light
        if pedestrian is not None:
            self.pedestrian = pedestrian
        if vehicle is not None:
            self.vehicle = vehicle





# Print action message based on sensor status
def print_message(sensor):
    action = ""
    if sensor.light == "red" or sensor.pedestrian == "yes" or sensor.vehicle == "yes":
        action = "STOP"
    elif sensor.light == "green" and sensor.pedestrian == "no" and sensor.vehicle == "no":
        action = "PROCEED"
    elif sensor.light == "yellow" and sensor.pedestrian == "no" and sensor.vehicle == "no":
        action = "CAUTION"
    elif sensor.pedestrian == "yes":
        action = "STOP"
    elif sensor.vehicle == "yes":
        action = "STOP"
    else:
        action = "Proceed"
    print(f"\n=== {action} ===")
    print(f"Light: {sensor.light}")
    print(f"Pedestrian: {sensor.pedestrian}")
    print(f"Vehicle: {sensor.vehicle}\n")




# Main function to run the program
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    sensor = Sensor()
    while True:
        try:
            status = input("Select 1 For Light, 2 for pexdestrian, 3 for vehicle, or 0 to end the program: ")
            if status not in ["0", "1", "2", "3"]:
                raise ValueError("Invalid menu option.")
        except ValueError:
            print("Invalid input. Please enter 0, 1, 2, or 3.\n")
            continue

        if status == "0":
            print("\nProgram ended.")
            break
        if status == "1":
            light = input("What change has been identified? (green, yellow, red) (Case Sensitive): ")
            if light not in ["green", "yellow", "red"]:
                print("Invalid input! Light must be 'green', 'yellow', or 'red'.\n")
                continue
            sensor.update_status(light = light)
        elif status == "2":
            pedestrian = input("What change has been identified? (yes or no):  ")
            if pedestrian not in ["yes", "no"]:
                print("Invalid vision change.\n")
                continue
            sensor.update_status(pedestrian = pedestrian)
        elif status == "3":
            vehicle = input("What change has been identified (yes or no): ")
            if vehicle not in ["yes", "no"]:
                print("Invalid vision change.\n")
                continue
            sensor.update_status(vehicle = vehicle)

        print_message(sensor)

# Run main if this file is executed
# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
       main()
