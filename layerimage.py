import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
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
        #still working on this!!
        print("Hello World girl idk")

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
test = tk.Label(window, image=crimson)
test.pack()

window.mainloop()