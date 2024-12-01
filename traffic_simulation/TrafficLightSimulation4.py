import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk

from DefaultCountdownTraffic2and4 import green_traffic_up_right_countdown, green_traffic_left_countdown, yellow_traffic_countdown
from DefaultCountdownTraffic1and3 import red_traffic_countdown

def traffic_light_simulation_4():
    # Create the main application window
    root = tk.Tk()
    root.title("Traffic Light 4")

    # Set the size of the main window to 600x400
    root.geometry("580x400")
    root.resizable(False, False)

    # Create a Canvas to draw shapes and add an image
    canvas = tk.Canvas(root, width=580, height=400, bg="white")
    canvas.pack(fill="both", expand=True)

    # Draw a rectangle 1
    canvas.create_rectangle(
        10.2, 263.5, 384.9, 379.5,
        fill="black",
        outline="",
        width=2
    )

    canvas.create_rectangle(
        138.8, 6.5, 254.8, 379.5,
        fill="black",
        outline="",
        width=2
    )

    canvas.create_rectangle(
        392.2, 23.9, 525.3, 108.1,
        fill="black",
        outline="",
        width=2
    )

    traffic_light_countdown = canvas.create_text(
        458, 63,
        text="87",
        font=font.Font(family="Montserrat", size=64, weight="bold"),
        fill="white"
    )

    # Circle dimensions
    width, height = 105.9, 105.9

    # Draw the 5 circles
    # Circle 1
    canvas.create_oval(
        20.8, 268.6, 20.8 + width, 268.6 + height,
        fill="white",
        outline=""
    )

    # Circle 2
    canvas.create_oval(
        143.7, 268.6, 143.7 + width, 268.6 + height,
        fill="white",
        outline=""
    )

    # Circle 3
    canvas.create_oval(
        267.6, 268.6, 267.6 + width, 268.6 + height,
        fill="white",
        outline=""
    )

    # Circle 4
    yellow_light = canvas.create_oval(
        143.7, 145.2, 143.7 + width, 145.2 + height,
        fill="white",
        outline=""
    )

    # Circle 5
    red_light = canvas.create_oval(
        143.7, 16, 143.7 + width, 16 + height,
        fill="white",
        outline=""
    )

    # Load and display an image
    try:
        image = Image.open("D:/Project/image/cctv-camera.png")
        image = image.resize((138, 138))
        photo = ImageTk.PhotoImage(image)
        canvas.create_image(500, 320, image=photo, anchor="center")
    except Exception as e:
        print(f"Error loading image: {e}")

    def green_traffic_light_arrow_up_right():
        # Load and resize the images
        image1 = Image.open("D:/Project/image/up-arrow-green.png").resize((90, 90))
        photo1 = ImageTk.PhotoImage(image1)

        image2 = Image.open("D:/Project/image/right-arrow-green.png").resize((90, 90))
        photo2 = ImageTk.PhotoImage(image2)

        # Store references to prevent garbage collection
        canvas.image1 = photo1
        canvas.image2 = photo2

        # Place the images on the canvas
        canvas.up_arrow_green = canvas.create_image(198, 320.9, image=photo1, anchor="center")
        canvas.right_arrow_green = canvas.create_image(325, 320.9, image=photo2, anchor="center")

    def remove_green_traffic_light_arrow_up_right():
        canvas.delete(canvas.up_arrow_green)
        canvas.delete(canvas.right_arrow_green)

    def green_traffic_light_arrow_left():
        # Load and resize the images
        image = Image.open("D:/Project/image/left-arrow-green.png").resize((90, 90))
        photo = ImageTk.PhotoImage(image)

        # Store references to prevent garbage collection
        canvas.image = photo

        # Place the image on the canvas
        canvas.left_arrow_green = canvas.create_image(72, 320.9, image=photo, anchor="center")

    def remove_green_traffic_light_arrow_left():
        canvas.delete(canvas.left_arrow_green)

    def red_traffic_light_arrow_up_right():
        # Load and resize the images
        image1 = Image.open("D:/Project/image/up-arrow-red.png").resize((90, 90))
        photo1 = ImageTk.PhotoImage(image1)

        image2 = Image.open("D:/Project/image/right-arrow-red.png").resize((90, 90))
        photo2 = ImageTk.PhotoImage(image2)

        # Store references to prevent garbage collection
        canvas.image1 = photo1
        canvas.image2 = photo2

        # Place the images on the canvas
        canvas.up_arrow_red = canvas.create_image(198, 320.9, image=photo1, anchor="center")
        canvas.right_arrow_red = canvas.create_image(325, 320.9, image=photo2, anchor="center")

    def remove_red_traffic_light_arrow_up_right():
        canvas.delete(canvas.up_arrow_red)
        canvas.delete(canvas.right_arrow_red)

    def red_traffic_light_arrow_left():
        # Load and resize the images
        image = Image.open("D:/Project/image/left-arrow-red.png").resize((90, 90))
        photo = ImageTk.PhotoImage(image)

        # Store references to prevent garbage collection
        canvas.image = photo

        # Place the image on the canvas
        canvas.left_arrow_red = canvas.create_image(72, 320.9, image=photo, anchor="center")

    def remove_red_traffic_light_arrow_left():
        canvas.delete(canvas.left_arrow_red)


    def green_traffic_up_right(count):
        """
        So when the light turns green, you can only go forward and turn right.
        You're not able to turn left yet.
        """
        green_traffic_light_arrow_up_right()
        red_traffic_light_arrow_left()
        if count > 0:
            # Update countdown text and color
            canvas.itemconfig(traffic_light_countdown, text=count, fill="#34b549")
            canvas.after(1000, green_traffic_up_right, count - 1)  # Schedule the next countdown
        else:
            # After forward and right end, transition to left turn
            green_traffic_left(green_traffic_left_countdown)

    def green_traffic_left(count):
        """
        Now you're able to turn left
        """
        remove_green_traffic_light_arrow_up_right()
        remove_red_traffic_light_arrow_left()

        red_traffic_light_arrow_up_right()
        green_traffic_light_arrow_left()

        if count > 0:
            canvas.itemconfig(traffic_light_countdown, text=count, fill="#34b549")
            canvas.after(1000, green_traffic_left, count - 1)  # Schedule the next countdown
        else:
            # After yellow light ends, transition to red light
            yellow_traffic(yellow_traffic_countdown)

    def yellow_traffic(count):
        """
        When the light turns yellow, remove all arrows.
        """
        remove_red_traffic_light_arrow_up_right()
        remove_green_traffic_light_arrow_left()

        if count > 0:
            # Update countdown text and color
            canvas.itemconfig(yellow_light, fill="#ffd230")
            canvas.itemconfig(traffic_light_countdown, text=count, fill="#ffd230")
            canvas.after(1000, yellow_traffic, count - 1)  # Schedule the next countdown
        else:
            # After yellow light ends, transition to red light
            canvas.itemconfig(yellow_light, fill="white")
            red_traffic(red_traffic_countdown)

    def red_traffic(count):
        red_traffic_light_arrow_up_right()
        red_traffic_light_arrow_left()
        if count > 0:
            # Update countdown text and color
            canvas.itemconfig(red_light, fill="red")
            canvas.itemconfig(traffic_light_countdown, text=count, fill="red")
            canvas.after(1000, red_traffic, count - 1)  # Schedule the next countdown
        else:
            # After red light ends, transition back to green-light
            canvas.itemconfig(red_light, fill="white")
            remove_red_traffic_light_arrow_up_right()
            remove_red_traffic_light_arrow_left()
            green_traffic_up_right(green_traffic_up_right_countdown)

    red_traffic(red_traffic_countdown)

    # Run the Tkinter event loop
    root.mainloop()