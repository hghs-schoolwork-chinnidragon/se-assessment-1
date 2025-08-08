import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Avatar")
# crimson = tk.PhotoImage(file="images/crimson.png")
# chair = tk.PhotoImage(file="images/chair.png")
# print(crimson.width()/2, crimson.height()/2)
# crimson = crimson.resize((517, 600))
class Avatars:
    def __init__(self, pathToBase, pathToHair, pathToMouth, pathToAccesory):
        self.__base = pathToBase
        self.__hair = pathToHair
        self.__mouth = pathToMouth
        self.__accessories = pathToAccesory

    def createAvatar(self):
        #creating the images based on the path provided
        base = Image.open(self.__base)
        hair = Image.open(self.__hair)
        mouth = Image.open(self.__mouth)
        #putting all the images together as the avatar
        accessories = Image.open(self.__accesories)
        base.paste(hair, (0, 0), hair)
        base.paste(mouth, (0, 0), mouth)
        base.paste(accessories, (0, 0), accessories)

def resize(height):
    width = height*517/600
    return width

# print(resize(600))

crimson = Image.open("images/crimson.png")
crimson = crimson.resize((517, 600))
chair = Image.open("images/chair.png")
chair = chair.resize((517, 600))
crimson.paste(chair, (0, 0), chair)

crimson =  ImageTk.PhotoImage(crimson)
chair = ImageTk.PhotoImage(chair)
test = tk.Label(window, image=crimson)

def addHair():
    crimson = Image.open("images/crimson.png")
    crimson = Image.open("images/crimson.png")
    crimson = crimson.resize((517, 600))
    chair = Image.open("images/chair.png")
    chair = chair.resize((517, 600))
    crimson.paste(chair, (0, 0), chair)

# test.pack(padx=0,pady=0)
# test2 = tk.Label(window, image=chair)
# test2.pack(padx=0,pady=0)

window.mainloop()