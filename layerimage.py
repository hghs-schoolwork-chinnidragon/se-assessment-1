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
    def __init__(self, image_paths):
        print(image_paths)
        self.__accessories = image_paths[0]
        self.__hair = image_paths[1]
        self.__mouth = image_paths[2]
        self.__pant = image_paths[3]
        self.__base = image_paths[4]
        self.__shirt = image_paths[5]
        self.__shoe = image_paths[6]
        self.__active_attr = []
        print(self.getImages())

    def resizeImg(self, newWidth, image):
        #newwidth divided by width/height OR newwidth * height/width
        #resizing the image while keeping the aspect ratio
        pilImage = Image.open(image)
        print (f"{pilImage.width}x{pilImage.height}")
        ratio = pilImage.width/pilImage.height
        newHeight = round(newWidth*ratio)
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
        for item in self.__active_attr:
            print(item)
            base = self.getImages()
            base = base[4]
            base.paste(item, (0,0), item)
            print(base)

        avatar =  ImageTk.PhotoImage(base)
        try:
            avatarLabel.config(window, image=avatar)
        except NameError:
            avatarLabel = tk.Label(window, image=avatar)
        avatarLabel.image=avatar
        avatarLabel.grid(sticky="s", column=6, columnspan=1)
    
    def saveAvatar(self, filename):
        data = {
            "attributes":self.__active_attr
        }
        with open(f'{filename}', 'w') as file:
            json.dump(data, file)


crimsonImages = []
for image in sorted(os.listdir("images/crimson")):
    crimsonImages.append(f"images/crimson/{image}")


crimsonAvatar = Avatars(crimsonImages)

imglist = []
# for image in crimsonAvatar.getImages():
#     print(image)
#     imglist.append(crimsonAvatar.resizeImg(100, image))

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