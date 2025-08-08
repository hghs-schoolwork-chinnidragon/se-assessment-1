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
    def __init__(self, image_paths, jsonfile):
        #DEBUG
        # print(image_paths)
        self.__accessories = image_paths[0]
        self.__hair = image_paths[1]
        self.__mouth = image_paths[2]
        self.__pant = image_paths[3]
        self.__base = image_paths[4]
        self.__shirt = image_paths[5]
        self.__shoe = image_paths[6]
        try:
            with open(jsonfile, "r") as file:
                attributes = json.load(file)
            self.__active_attr = attributes["attributes"]
        except TypeError: #no file has been passed
            print("CAN YOU KYS HAHAH!!!")
            self.__active_attr = []
        #DEBUG
        # print(self.getImages())

    def resizeImg(self, newWidth, image):
        #newwidth divided by width/height OR newwidth * height/width
        #resizing the image while keeping the aspect ratio
        pilImage = Image.open(image)
        print (f"{pilImage.width}*{pilImage.height}")
        ratio = pilImage.width/pilImage.height
        newHeight = round(newWidth/ratio)
        resizedImage = pilImage.resize([newWidth, newHeight])
        # print(f"resized! dimensions {resizedImage.width}x{resizedImage.height}")
        return(resizedImage)

    
    def getImages(self):
        return [
            self.__accessories,
            self.__hair,
            self.__mouth,
            self.__pant,
            self.__base,
            self.__shirt,
            self.__shoe
        ]
    
    def setImages(self, images):
        self.__accessories = images[0]
        self.__hair = images[1]
        self.__mouth = images[2]
        self.__pant = images[3]
        self.__base = images[4]
        self.__shirt = images[5]
        self.__shoe = images [6]

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

    #toggling various outfit options
    def togglePant(self):
        if self.__pant in self.__active_attr:
            self.__active_attr.remove(self.__pant)
        else:
            self.__active_attr.append(self.__pant)
        print(self.__active_attr)
        self.activateAvatar()

    def toggleMouth(self):
        if self.__mouth in self.__active_attr:
            self.__active_attr.remove(self.__mouth)
        else:
            self.__active_attr.append(self.__mouth)
        print(self.__active_attr)
        self.activateAvatar()

    def toggleHair(self):
        if self.__hair in self.__active_attr:
            self.__active_attr.remove(self.__hair)
        else:
            self.__active_attr.append(self.__hair)
        print(self.__active_attr)
        self.activateAvatar()

    def toggleShirt(self):
        if self.__shirt in self.__active_attr:
            self.__active_attr.remove(self.__shirt)
        else:
            self.__active_attr.append(self.__shirt)
        print(self.__active_attr)
        self.activateAvatar()

    def toggleAccessory(self):
        if self.__accessories in self.__active_attr:
            self.__active_attr.remove(self.__accessories)
        else:
            self.__active_attr.append(self.__accessories)
        print(self.__active_attr)
        self.activateAvatar()

    def activateAvatar(self):
        base = self.__base.copy() 
        if not self.__active_attr: #If there aren't any active attributes
            avatar =  ImageTk.PhotoImage(base) #Default to the bare base
        else:
            for item in self.__active_attr:
                # print(item)
                # base = self.getImages()
                # base = base[4]
                base.paste(item, (0,0), item)
                print(base)
                avatar =  ImageTk.PhotoImage(base)

        if not hasattr(self, 'avatarLabel'):
            self.avatarLabel = tk.Label(window, image=avatar)
            self.avatarLabel.grid(column=6, columnspan=1)
        else:
            self.avatarLabel.config(image=avatar)
        self.avatarLabel.image = avatar 
        # avatarLabel = tk.Label(window, image=avatar)
        # avatarLabel.image=avatar
        # avatarLabel.grid(column=6, columnspan=1)
    
    #for saving the current attributes (so that the avatar will look the same wherever)
    def saveAvatar(self, filename):
        for item in self.__active_attr:
            print(item)
        # data = {
        #     "attributes":self.__active_attr
        # }
        # with open(filename, 'w') as file:
        #     json.dump(data, file)


crimsonImages = []
for image in sorted(os.listdir("images/crimson")):
    crimsonImages.append(f"images/crimson/{image}")


crimsonAvatar = Avatars(crimsonImages, None)

imglist = []
for image in crimsonAvatar.getImages():
    print(image)
    imglist.append(crimsonAvatar.resizeImg(100, image))

crimsonAvatar.setImages(imglist)
# crimsonAvatar.createAvatar()



# while True:
hairButton = tk.Button(window, text="Hair", command=crimsonAvatar.toggleHair)
hairButton.grid(row=7, column=0)

mouthButton = tk.Button(window, text="Mouth", command=crimsonAvatar.toggleMouth)
mouthButton.grid(row=7, column=1)

shirtButton = tk.Button(window, text="Shirt", command=crimsonAvatar.toggleShirt)
shirtButton.grid(row=7, column=2)

pantButton = tk.Button(window, text="Pant", command=crimsonAvatar.togglePant)
pantButton.grid(row=7, column=3)


accessoryButton = tk.Button(window, text="Accessory", command=crimsonAvatar.toggleAccessory)
accessoryButton.grid(row=7, column=4)

def save():
    crimsonAvatar.saveAvatar("activeattributes.json")

saveButton = tk.Button(window, text="Save", command=save)
saveButton.grid(row=7, column=5)



window.mainloop()