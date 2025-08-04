import tkinter as tk
from PIL import Image, ImageTk
import os
import json

window = tk.Tk()
# crimson = tk.PhotoImage(file="images/crimson.png")
# chair = tk.PhotoImage(file="images/chair.png")
# print(crimson.width()/2, crimson.height()/2)
# crimson = crimson.resize((517, 600))
class Avatars:
    def __init__(self, pathToBase, pathToHair, pathToMouth, pathToAccesory, pathToShirt, resizeParams):
        self.__base = pathToBase
        self.__hair = pathToHair
        self.__mouth = pathToMouth
        self.__shirt = pathToShirt
        self.__accessories = pathToAccesory
        self.__active_attr = []
        self.resizeParams = resizeParams

    def resizeImg(self, newWidth, image):
        newLength = self.resizeParams[1]*self.resizeParams[0]/newWidth
        image = image.resize(newWidth, newLength)
        return(image)
    
    def getImages(self):
        return [self.__accessories, self.__hair, self.__mouth, self.__base, self.__shirt]
    
    def setImages(self, images):
        self.__base = pathToBase
        self.__hair = pathToHair
        self.__mouth = pathToMouth
        self.__shirt = pathToShirt
        self.__accessories = pathToAccesory

    def createAvatar(self):
        #creating the images based on the path provided
        self.__base = Image.open(self.__base)
        self.__hair = Image.open(self.__hair)
        self.__mouth = Image.open(self.__mouth)
        self.__accessories = Image.open(self.__accessories)
        self.__shirt = Image.open(self.__shirt)

    
    def toggleHair(self):
        if self.__hair in self.__active_attr:
            self.__active_attr.remove(self.__hair)
        else:
            self.__active_attr.append(self.__hair)
        print(self.__active_attr)

    def toggleMouth(self):
        if self.__mouth in self.__active_attr:
            self.__active_attr.remove(self.__mouth)
        else:
            self.__active_attr.append(self.__mouth)
        print(self.__active_attr)

    def toggleHair(self):
        if self.__hair in self.__active_attr:
            self.__active_attr.remove(self.__hair)
        else:
            self.__active_attr.append(self.__hair)
        print(self.__active_attr)

    def toggleShirt(self):
        if self.__shirt in self.__active_attr:
            self.__active_attr.remove(self.__shirt)
        else:
            self.__active_attr.append(self.__shirt)
        print(self.__active_attr)


    def toggleAccessory(self):
        if self.__accessories in self.__active_attr:
            self.__active_attr.remove(self.__accessories)
        else:
            self.__active_attr.append(self.__accessories)
        print(self.__active_attr)

    def activateAvatar(self):
        for item in self.__active_attr:
            print(item)
            self.__base.paste(item, (0,0), item)
        avatar =  ImageTk.PhotoImage(self.__base)
        avatarLabel = tk.Label(window, image=avatar)
        avatarLabel.grid(
            row=0,
            column=0,
            # columnspan=5
        )
    
    def saveAvatar(self, filename):
        data = {
            "attributes":self.__active_attr
        }
        with open(f'{filename}', 'w') as file:
            json.dump(data, file)

    # def resize(height):
    #     width = height*517/600
    #     return width

# print(resize(600))

crimsonAvatar = Avatars(
    "images/crimson.png", 
    "images/chair.png", 
    "images/cmouth.png", 
    "images/caccess.png", 
    "images/cshirt.png", 
    (464, 568)  # Resize parameters are not used in this code, but can be used for resizing images if needed
    )

for image in crimsonAvatar.getImages():
    crimsonAvatar.resizeImg(100, image)
crimsonAvatar.createAvatar()

# while True:
hairButton = tk.Button(window, text="Hair", command=crimsonAvatar.toggleHair)
hairButton.grid(row=7, column=0)

mouthButton = tk.Button(window, text="Mouth", command=crimsonAvatar.toggleMouth)
mouthButton.grid(row=7, column=1)

shirtButton = tk.Button(window, text="Shirt", command=crimsonAvatar.toggleShirt)
shirtButton.grid(row=7, column=2)

accessoryButton = tk.Button(window, text="Accessory", command=crimsonAvatar.toggleAccessory)
accessoryButton.grid(row=7, column=3)

saveButton = tk.Button(window, text="Save", command=crimsonAvatar.activateAvatar)
saveButton.grid(row=7, column=4)



window.mainloop()

print(os.access("images", 1))
# crimson = Image.open("images/crimson.png")
# crimson = crimson.resize((517, 600))
# chair = Image.open("images/chair.png")
# chair = chair.resize((517, 600))
# cmouth = Image.open("images/cmouth.png")
# cmouth = cmouth.resize((517, 600))
# cshirt = Image.open("images/cshirt.png")
# cshirt = cshirt.resize((517, 600))



# def addremoveHair(currentattributes):
#     for item in currentattributes:
#         crimson.paste(item, (0,0), item)
#     crimson.paste(chair, (0,0), chair)
    


# for item in self.__active_attr:
#     crimson.paste(item, (0, 0), item)



# def reset():
#     crimson = Image.open("images/crimson.png")

# def addHair():
#     crimson = Image.open("images/crimson.png")
#     crimson = Image.open("images/crimson.png")
#     crimson = crimson.resize((517, 600))
#     chair = Image.open("images/chair.png")
#     chair = chair.resize((517, 600))
#     crimson.paste(chair, (0, 0), chair)


# test2 = tk.Label(window, image=chair)
# test2.pack(padx=0,pady=0)

window.mainloop()