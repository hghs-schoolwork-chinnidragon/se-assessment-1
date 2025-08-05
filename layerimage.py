import tkinter as tk
from PIL import Image, ImageTk
import os
import json

window = tk.Tk()
# crimson = tk.PhotoImage(file="images/crimson.png")
# chair = tk.PhotoImage(file="images/chair.png")
# print(crimson.width()/2, crimson.height()/2)
# crimson = crimson.resize((517, 600))

#['caccess.png', ' 
# 'chair.png', 'cmouth.png', , 'cpant.png', 
# 'crimson.png', 'cshirt.png', 'cshoe.png']
class Avatars:
    def __init__(self, image_paths, resizeParams):
        self.__accessories = image_paths[0]
        self.__hair = image_paths[1]
        self.__mouth = image_paths[2]
        self.__pant = image_paths[3]
        self.__base = image_paths[4]
        self.__shirt = image_paths[5]
        self.__shoe = image_paths[6]
        self.__active_attr = []
        self.resizeParams = resizeParams

    def resizeImg(self, newWidth, image):
        newLength = round(self.resizeParams[1]*self.resizeParams[0]/newWidth)
        image = Image.open(image)
        image = image.resize([newWidth, newLength])
        return(image)
    
    def getImages(self):
        return [self.__base, self.__hair, self.__mouth, self.__shirt, self.__accessories]
    
    def setImages(self, images):
        self.__base = images[0]
        self.__hair = images[1]
        self.__mouth = images[2]
        self.__shirt = images[3]
        self.__accessories = images[4]

    def createAvatar(self):
        #creating the images based on the path provided
        try:
            self.__base = Image.open(self.__base)
            self.__hair = Image.open(self.__hair)
            self.__mouth = Image.open(self.__mouth)
            self.__accessories = Image.open(self.__accessories)
            self.__shirt = Image.open(self.__shirt)
        except AttributeError: #raised when they are already images (eg resize function has been used)
            pass

    
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
            print(self.__base)

        # avatar =  ImageTk.PhotoImage(self.__base)
        avatar = Image.open("images/oof.png")
        newavatar = ImageTk.PhotoImage(avatar)
        avatarLabel = tk.Label(window, image=newavatar, text="sweet fading star", compound="top")
        avatarLabel.grid(sticky="s", rowspan="5", column=6)
    
    def saveAvatar(self, filename):
        data = {
            "attributes":self.__active_attr
        }
        with open(f'{filename}', 'w') as file:
            json.dump(data, file)

print(f"images/crimson/{sorted(os.listdir("images/crimson"))}")

crimsonImages = []
for image in sorted(os.listdir("images/crimson")):
    crimsonImages.append(f"images/crimson/{image}")

crimsonAvatar = Avatars(crimsonImages,(464, 568))

imglist = []
for image in crimsonAvatar.getImages():
    print(image)
    imglist.append(crimsonAvatar.resizeImg(100, image))

crimsonAvatar.setImages(imglist)
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