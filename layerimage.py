import tkinter as tk
from PIL import Image, ImageTk
import os
import json

window = tk.Tk()
window.title = "avatar customisation"
# window.config(background="#D5FBFF")
window.geometry("600x600+450+50")

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
        self.__attr_map = {
                    "accessories": self.__accessories,
                    "hair": self.__hair,
                    "mouth": self.__mouth,
                    "pant": self.__pant,
                    "base": self.__base,
                    "shirt": self.__shirt,
                    "shoe": self.__shoe,
                }
        try:
            with open(jsonfile, "r") as file:
                attributes = json.load(file)
            self.__active_attr = attributes["attributes"]
            print(self.__active_attr)
        except TypeError: #no file has been passed
            print("no file has been provided :(")
            self.__active_attr = []
        # self.activateAvatar()
        #DEBUG
        # print(self.getImages())

    def resizeImg(self, newWidth, image):
        #newwidth divided by width/height OR newwidth * height/width
        #resizing the image while keeping the aspect ratio
        pilImage = Image.open(image).convert("RGBA")
        print (f"{pilImage.width}/{pilImage.height}")
        # ratio = pilImage.width/pilImage.height
        orig_width, orig_height = pilImage.size
        ratio = orig_width / orig_height
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
        self.__attr_map = {
                    "accessories": self.__accessories,
                    "hair": self.__hair,
                    "mouth": self.__mouth,
                    "pant": self.__pant,
                    "base": self.__base,
                    "shirt": self.__shirt,
                    "shoe": self.__shoe,
                }

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
        if "pant" in self.__active_attr:
            self.__active_attr.remove("pant")
        else:
            self.__active_attr.append("pant")
        print(self.__active_attr)
        self.activateAvatar()

    def toggleMouth(self):
        if "mouth" in self.__active_attr:
            self.__active_attr.remove("mouth")
        else:
            self.__active_attr.append("mouth")
        print(self.__active_attr)
        self.activateAvatar()

    def toggleHair(self):
        if "hair" in self.__active_attr:
            self.__active_attr.remove("hair")
        else:
            self.__active_attr.append("hair")
        print(self.__active_attr)
        self.activateAvatar()

    def toggleShirt(self):
        if "shirt" in self.__active_attr:
            self.__active_attr.remove("shirt")
        else:
            self.__active_attr.append("shirt")
        print(self.__active_attr)
        self.activateAvatar()

    def toggleAccessory(self):
        if "accessories" in self.__active_attr:
            self.__active_attr.remove("accessories")
        else:
            self.__active_attr.append("accessories")
        print(self.__active_attr)
        self.activateAvatar()

    def activateAvatar(self):
        base = self.__base.copy() 
        if not self.__active_attr: #If there aren't any active attributes
            avatar =  ImageTk.PhotoImage(base) #Default to the bare base
        else:
            for item in self.__active_attr:
                mappedItem = self.__attr_map[item]
                # print(mappedItem)
                # # base = self.getImages()
                # # base = base[4]
                # base.paste(attr_map[str(item)], (0,0), (attr_map[str(item)]))
                base.paste(mappedItem), (0,0), (mappedItem)
                # print(base)
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
        data = {
                "attributes": []
                
            }
        for i in range(0, len(self.__active_attr)):
            data["attributes"].append(str(self.__active_attr[i]))
        print(data)
        with open(filename, 'w') as file:
            json.dump(data, file)
        quit()


crimsonImages = []
for image in sorted(os.listdir("images/crimson")):
    crimsonImages.append(f"images/crimson/{image}")


crimsonAvatar = Avatars(crimsonImages, "activeattributes.json")

imglist = []
for image in crimsonAvatar.getImages():
    print(image)
    imglist.append(crimsonAvatar.resizeImg(200, image))

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

# crimsonAvatar.activateAvatar()


window.mainloop()