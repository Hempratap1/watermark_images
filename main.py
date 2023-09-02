import time
from tkinter import *
from PIL import Image, ImageDraw, ImageFont, ImageTk


def add_it():
    my_image = Image.open("images/rename.png")
    text_font = ImageFont.truetype("arial.ttf", 46)
    text_to_add = my_entry.get()
    edit_image = ImageDraw.Draw(my_image)
    edit_image.text((150, 300), text_to_add, "red", font=text_font)
    my_image.save("images/results.png")

    my_entry.delete(0, END)
    my_entry.insert(0, "Saving file...")
    time.sleep(3)
    show_pic()
    my_entry.delete(0, END)


def show_pic():
    global images
    images = Image.open('images/results.png')
    images = images.resize((300, 300), Image.NEAREST)  # Resize without anti-aliasing
    images = ImageTk.PhotoImage(images)
    my_label.config(image=images)
    my_label.image = images  # Keep a reference


root = Tk()
root.title('Watermark App')
root.geometry('650x650')

# Load the image
image_path = "images/rename.png"
original_image = Image.open(image_path)

# Calculate the aspect ratio to fit within the available space
width, height = original_image.size
max_width = 600  # Adjust this value to fit your screen
max_height = 600  # Adjust this value to fit your screen
aspect_ratio = min(max_width / width, max_height / height)

# Resize the image to fit within the available space without anti-aliasing
resized_image = original_image.resize(
    (int(width * aspect_ratio), int(height * aspect_ratio)), Image.NEAREST
)

# Convert the resized image to a PhotoImage
photo = ImageTk.PhotoImage(resized_image)

my_label = Label(root, image=photo)
my_label.pack(pady=20)

my_entry = Entry(root, font=("Helvetica", 24))
my_entry.pack(padx=20)

my_button = Button(root, text='Add text to image', command=add_it, font=("Helvetica", 24))
my_button.pack(pady=20)

root.mainloop()

