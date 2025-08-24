import tkinter as tk
from PIL import Image, ImageTk
import json
class Avatars:
    def __init__(self, image_paths, jsonfile, window, canvas=None):
        # Store references to window, canvas, and JSON file for avatar attributes
        self.__window = window
        self.jsonfile = jsonfile
        self.__canvas = canvas

        # Load image paths for each avatar layer
        self.__accessories = image_paths[0]
        self.__hair = image_paths[1]
        self.__mouth = image_paths[2]
        self.__pant = image_paths[3]
        self.__base = image_paths[4]
        self.__shirt = image_paths[5]
        self.__shoe = image_paths[6]

        # List and map for easy attribute access
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

        # Load active attributes from JSON file, or start empty if not provided
        try:
            with open(self.jsonfile, "r") as file:
                attributes = json.load(file)
            self.__active_attr = attributes["attributes"]
        except TypeError: # no file has been passed
            print("no file has been provided :(")
            self.__active_attr = []

    def resizeImg(self, newWidth, image):
        # Resize an image while maintaining aspect ratio
        pilImage = Image.open(image).convert("RGBA")
        orig_width, orig_height = pilImage.size
        ratio = orig_width / orig_height
        newHeight = round(newWidth/ratio)
        resizedImage = pilImage.resize([newWidth, newHeight])
        return resizedImage
    
    def getImages(self):
        # Return all avatar layer images in order
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
        # Set avatar layer images from a provided list
        self.__accessories = images[0]
        self.__hair = images[1]
        self.__mouth = images[2]
        self.__pant = images[3]
        self.__base = images[4]
        self.__shirt = images[5]
        self.__shoe = images[6]
        # Update attribute map with new images
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
        # Open image files for each layer if not already opened
        try:
            self.__base = Image.open(self.__base)
            self.__hair = Image.open(self.__hair)
            self.__mouth = Image.open(self.__mouth)
            self.__accessories = Image.open(self.__accessories)
            self.__shirt = Image.open(self.__shirt)
        except AttributeError: # Already PIL images
            pass

    # Toggle functions for each outfit option
    def togglePant(self):
        # Add/remove pants from active attributes
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
        # Duplicate toggle for shoe (can be removed if not needed)
        if "shoe" in self.__active_attr:
            self.__active_attr.remove("shoe")
        else:
            self.__active_attr.append("shoe")
        self.activateAvatar()

    def activateAvatar(self, x=200, y=200):
        # Compose the avatar image by layering active attributes
        base = self.__base.copy() 
        if not self.__active_attr: # If no attributes, show base only
            avatar = ImageTk.PhotoImage(base)
        else:
            for item in self.__active_attr:
                mappedItem = self.__attr_map[item]
                base.paste(mappedItem, (0,0), mappedItem)
                avatar = ImageTk.PhotoImage(base)
        if self.__canvas:
            # Display avatar on canvas
            self.__canvas.delete("avatar")  # Remove previous avatar
            self.__canvas.create_image(x, y, image=avatar, tags="avatar")
            self.__canvas.image = avatar    # Prevent garbage collection
        else:
            # Display avatar in a label if no canvas is provided
            self.avatarLabel.image = avatar 
            if not hasattr(self, 'avatarLabel'):
                self.avatarLabel = tk.Label(self.__window, image=avatar)
                self.avatarLabel.grid(column=6, columnspan=1)
            else:
                self.avatarLabel.config(image=avatar)
            self.avatarLabel.image = avatar 
    
    def saveAvatar(self, filename):
        # Save current active attributes to a JSON file
        data = {
            "attributes": []
        }
        for i in range(0, len(self.__active_attr)):
            data["attributes"].append(str(self.__active_attr[i]))
        with open(filename, 'w') as file:
            json.dump(data, file)
        self.__window.destroy()
    
    def reset(self):
        # Reset avatar to base (no attributes)
        self.__active_attr = []
        self.activateAvatar()

    def create_Buttons(self):
        # Create and place buttons for toggling each attribute on the canvas
        hairButton = tk.Button(self.__window, text="Hair", command=self.toggleHair, font=("Noteworthy", 10))
        self.__canvas.create_window(300, 0, anchor="nw", window=hairButton)

        mouthButton = tk.Button(self.__window, text="Mouth", command=self.toggleMouth, font=("Noteworthy", 10))
        self.__canvas.create_window(300, 50, anchor="nw", window=mouthButton)

        shirtButton = tk.Button(self.__window, text="Shirt", command=self.toggleShirt, font=("Noteworthy", 10))
        self.__canvas.create_window(300, 100, anchor="nw", window=shirtButton)

        pantButton = tk.Button(self.__window, text="Pant", command=self.togglePant, font=("Noteworthy", 10))
        self.__canvas.create_window(300, 150, anchor="nw", window=pantButton)

        accessoryButton = tk.Button(self.__window, text="Accessory", command=self.toggleAccessory, font=("Noteworthy", 10))
        self.__canvas.create_window(300, 200, anchor="nw", window=accessoryButton)

        shoeButton = tk.Button(self.__window, text="Shoe", command=self.toggleShoe, font=("Noteworthy", 10))
        self.__canvas.create_window(300, 250, anchor="nw", window=shoeButton)

        resetButton = tk.Button(self.__window, text="Reset", command=self.reset, font=("Noteworthy", 10))
        self.__canvas.create_window(300, 300, anchor="nw", window=resetButton)
        
        def save():
            self.saveAvatar(self.jsonfile)

        saveButton = tk.Button(self.__window, text="Save", command=save, font=("Noteworthy", 10))
        self.__canvas.create_window(300, 350, anchor="nw", window=saveButton)
