import tkinter as tk
from PIL import Image, ImageTk
import os
import json

# window = tk.Tk()
class Avatars:
    def __init__(self, image_paths, jsonfile, window, canvas=None):
        self.__window = window
        self.__window.title("avatar customisation")
        self.jsonfile = jsonfile
        # window.config(background="#D5FBFF")
        self.__window.geometry("+500+100")
        self.__canvas = canvas
        self.__accessories = image_paths[0]
        self.__hair = image_paths[1]
        self.__mouth = image_paths[2]
        self.__pant = image_paths[3]
        self.__base = image_paths[4]
        self.__shirt = image_paths[5]
        self.__shoe = image_paths[6]
        self.__attr = [self.__mouth, self.__hair, self.__pant, self.__shirt, self.__shoe, self.__accessories]
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
            with open(self.jsonfile, "r") as file:
                attributes = json.load(file)
            self.__active_attr = attributes["attributes"]
        except TypeError: #no file has been passed
            print("no file has been provided :(")
            self.__active_attr = []



    def resizeImg(self, newWidth, image):
        #newwidth divided by width/height OR newwidth * height/width
        #resizing the image while keeping the aspect ratio
        pilImage = Image.open(image).convert("RGBA")

        orig_width, orig_height = pilImage.size
        ratio = orig_width / orig_height
        newHeight = round(newWidth/ratio)
        resizedImage = pilImage.resize([newWidth, newHeight])

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
        self.activateAvatar()

    def toggleMouth(self):
        if "mouth" in self.__active_attr:
            self.__active_attr.remove("mouth")
        else:
            self.__active_attr.append("mouth")
        self.activateAvatar()

    def toggleHair(self):
        if "hair" in self.__active_attr:
            self.__active_attr.remove("hair")
        else:
            self.__active_attr.append("hair")
        self.activateAvatar()

    def toggleShoe(self):
        if "shoe" in self.__active_attr:
            self.__active_attr.remove("shoe")
        else:
            self.__active_attr.append("shoe")
        self.activateAvatar()

    def toggleShirt(self):
        if "shirt" in self.__active_attr:
            self.__active_attr.remove("shirt")
        else:
            self.__active_attr.append("shirt")
        self.activateAvatar()

    def toggleAccessory(self):
        if "accessories" in self.__active_attr:
            self.__active_attr.remove("accessories")
        else:
            self.__active_attr.append("accessories")
        self.activateAvatar()
    
    def toggleShoe(self):
        if "shoe" in self.__active_attr:
            self.__active_attr.remove("shoe")
        else:
            self.__active_attr.append("shoe")
        self.activateAvatar()

    def activateAvatar(self):
        base = self.__base.copy() 
        if not self.__active_attr: #If there aren't any active attributes
            avatar =  ImageTk.PhotoImage(base) #Default to the bare base
        else:
            for item in self.__active_attr:
                mappedItem = self.__attr_map[item]
                base.paste(mappedItem, (0,0), mappedItem)
                avatar =  ImageTk.PhotoImage(base)
        if self.__canvas:
            # Clear previous image
            self.__canvas.delete("avatar")
            # Create image on canvas
            self.__canvas.create_image(200, 200, image=avatar, tags="avatar")
            self.__canvas.image = avatar
        else:
            self.avatarLabel.image = avatar 
            if not hasattr(self, 'avatarLabel'):
                self.avatarLabel = tk.Label(self.__window, image=avatar)
                self.avatarLabel.grid(column=6, columnspan=1)
            else:
                self.avatarLabel.config(image=avatar)
            self.avatarLabel.image = avatar 
        if self.__active_attr == ["accessories","hair","mouth","pant","base","shirt","shoe"]:
            ssstylish = tk.Label(text="Stylish!!!!", font=tk.Font.Font(family="Apple Chancery", size=36))
            self.canvas.create_window(150, 300, window=ssstylish)
    
    #for saving the current attributes (so that the avatar will look the same wherever)
    def saveAvatar(self, filename):
        data = {
                "attributes": []
            }
        for i in range(0, len(self.__active_attr)):
            data["attributes"].append(str(self.__active_attr[i]))
        with open(filename, 'w') as file:
            json.dump(data, file)
        self.__window.destroy()
    
    def reset(self):
        self.__active_attr = []
        self.activateAvatar()

    def create_Buttons(self):
        hairButton = tk.Button(self.__window, text="Hair", command=self.toggleHair)
        self.__canvas.create_window(300, 0, anchor="nw", window=hairButton)

        mouthButton = tk.Button(self.__window, text="Mouth", command=self.toggleMouth)
        self.__canvas.create_window(300, 50, anchor="nw", window=mouthButton)

        shirtButton = tk.Button(self.__window, text="Shirt", command=self.toggleShirt)
        self.__canvas.create_window(300, 100, anchor="nw", window=shirtButton)

        pantButton = tk.Button(self.__window, text="Pant", command=self.togglePant)
        self.__canvas.create_window(300, 150, anchor="nw", window=pantButton)

        accessoryButton = tk.Button(self.__window, text="Accessory", command=self.toggleAccessory)
        self.__canvas.create_window(300, 200, anchor="nw", window=accessoryButton)

        shoeButton = tk.Button(self.__window, text="Shoe", command=self.toggleShoe)
        self.__canvas.create_window(300, 250, anchor="nw", window=shoeButton)

        resetButton = tk.Button(self.__window, text="Reset", command=self.reset)
        self.__canvas.create_window(300, 300, anchor="nw", window=resetButton)
        
        def save():
            self.saveAvatar(self.jsonfile)

        saveButton = tk.Button(self.__window, text="Save", command=save)
        self.__canvas.create_window(300, 350, anchor="nw", window=saveButton)


# cobaltImages = []
# for image in sorted(os.listdir("images/cobalt")):
#     # Skip .DS_Store and any other hidden files
#     if not image.startswith('.'):
#         cobaltImages.append(f"images/cobalt/{image}")
# # Creating canvas
# canvas = tk.Canvas(window, width=400, height=400, bg="#A1E3FF")
# canvas.grid(row=0, column=6, rowspan=6, padx=10, pady=10)
# #Creating the avatar on the canvas
# cobaltAvatar = Avatars(cobaltImages, "bactiveattributes.json", window, canvas=canvas)
# imglist = []
# for image in cobaltAvatar.getImages():
#     imglist.append(cobaltAvatar.resizeImg(750, image))
# cobaltAvatar.setImages(imglist)
# cobaltAvatar.create_Buttons()
# cobaltAvatar.activateAvatar()


# window.mainloop()