from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog


def open_img():
    # Select the Imagename  from a folder
    x = openfilename()

    # opens the image
    img = Image.open(x)

    # resize the image and apply a high-quality down sampling filter
    img = img.resize((250, 250), Image.ANTIALIAS)

    # PhotoImage class is used to add image to widgets, icons etc
    img = ImageTk.PhotoImage(img)

    # create a label
    panel = Label(root, image=img)

    # set the image as img
    panel.image = img
    panel.grid(row=2)


def openfilename():
    # open file dialog box to select image
    # The dialogue box has a title "Open"
    filename = filedialog.askopenfilename(title='"pen')
    return filename


# Create a windoe
root = Tk()

# Set Title as Image Loader
root.title("Image Loader")

# Allow Window to be resizable
root.resizable(width=True, height=True)

# Create a button and place it into the window using grid layout
btn = Button(root, text='open image', command=open_img).grid(row=1, columnspan=4)
root.mainloop()


