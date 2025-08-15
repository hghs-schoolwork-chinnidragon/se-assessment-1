import quizmodule
import tkinter as tk
from PIL import Image, ImageTk
import layerimage
import os
class Menu:
    # @staticmethod
    # def createwindow():
    #     window = tk.Tk()

    def __init__(self, quizzes, root):
        # window = tk.tk()
        for widget in root.winfo_children():
            widget.destroy()
        root.title("Quiz Menu")
        root.geometry("1440x1024")
        quizWidgets = []
        self.images = []
        canvas = tk.Canvas(root, width=1420, height=1200)
        
        canvas.grid()
        for i in range(0, len(quizzes)):
            print(quizzes[i].getImage())
            quizWidgetImage = Image.open(f"{quizzes[i].getImage()}")
            print(quizWidgetImage)
            quizWidgetImage = quizmodule.Quiz.resizeImg(200, quizWidgetImage)
            quizWidgetImage = ImageTk.PhotoImage(quizWidgetImage)
            title = quizzes[i].getTitle()
            file = quizzes[i].getFile()
            print(file)
            #need to resize images
            def runQuiz(file=file):
                quiz = quizmodule.Quiz(file)
                print(file)
                quiz.run()

            quizWidget = tk.Button(
                canvas,
                text=title,
                image=quizWidgetImage, 
                compound="bottom", 
                font=("Arial", 16, "italic"), 
                wraplength="200", 
                command=runQuiz)
            self.images.append(quizWidgetImage)
            print(self.images)
            quizWidgets.append(quizWidget)

        coordinates = [[1420/2+100, 100], [1420/2+100, 400], [1420/2+400, 100], [1420/2+400, 400]]

        bg_img = Image.open("images/menubg.png")
        bg_img = quizmodule.Quiz.resizeImg(1420, bg_img)  
        bg_imgtk = ImageTk.PhotoImage(bg_img)
        canvas.create_image(0, 0, image=bg_imgtk, anchor="nw")
        canvas.bg_imgtk = bg_imgtk

        for widgetNum, widget in enumerate(quizWidgets):
            canvas.create_window(coordinates[widgetNum][0], coordinates[widgetNum][1], anchor="nw", window=widget)
        
        canvas.create_text(1420/2-500, 100, text="Choose your challenge:", font=("Arial", 65, "bold", "italic"), fill="#141615", width=445, anchor="nw")
        
        avatarimg = Image.open("images/avatarcustomisation.png")
        avatarimg = quizmodule.Quiz.resizeImg(300, avatarimg)
        avatar_photo = ImageTk.PhotoImage(avatarimg)  # Create photo image
        def avatar():
            window = tk.Toplevel(root)
            crimsonImages = []
            for image in sorted(os.listdir("images/crimson")):
                crimsonImages.append(f"images/crimson/{image}")
            # Creating canvas
            canvas = tk.Canvas(window, width=400, height=400, bg="#FFA1A1")
            canvas.grid(row=0, column=6, rowspan=6, padx=10, pady=10)
            #Creating the avatar on the canvas
            crimsonAvatar = layerimage.Avatars(crimsonImages, "activeattributes.json", window=window, canvas=canvas)
            imglist = []
            for image in crimsonAvatar.getImages():
                imglist.append(crimsonAvatar.resizeImg(200, image))
            crimsonAvatar.setImages(imglist)
            crimsonAvatar.create_Buttons()
            crimsonAvatar.activateAvatar()

        avatarimg_button = tk.Button(root, image=avatar_photo, text="Customise your avatar!!", command=avatar)  # Create label with image
        avatarimg_button.image = avatar_photo

        canvas.create_window(500-200, 500+50, window=avatarimg_button)
        
            

    

root = tk.Tk()
root.title("Welcome")
images = []

canvas = tk.Canvas(root, width=1420, height=1200)

canvas.grid()


bg_img = Image.open("images/welcomebg.png")
bg_img2 = quizmodule.Quiz.resizeImg(1420, bg_img)  
print("yay")
bg_imgtk = ImageTk.PhotoImage(bg_img2)
print("yay")
root.image = bg_imgtk 
root.image = bg_imgtk 
images.append(bg_imgtk)
canvas.create_image(0, 0, image=bg_imgtk, anchor="nw")

q_whatColourIsThat = quizmodule.Quiz("whatColourIsThat.json")
q_allAboutHSV = quizmodule.Quiz("allAboutHSV.json")
q_colourRelationships = quizmodule.Quiz("colourRelationships.json")
q_tiersOfColours = quizmodule.Quiz("tiersOfColours.json")


def menu():
    Menu([q_allAboutHSV, q_whatColourIsThat, q_colourRelationships, q_tiersOfColours], root=root)


menubutton = tk.Button(text="Begin the Crusade", bg="#15A702", command=menu)

canvas.create_text(
    1420/2, 300, 
    text="Welcome to....",
    font=("Arial", 24, "italic"), 
    fill="#141615"
    )
canvas.create_text(
    1420/2, 
    400, 
    text="Colour Crusaders", 
    font=("Arial", 72, "bold"), 
    fill="#141615"
    )
canvas.create_window(
    1420/2,
    700,
    window=menubutton)






root.mainloop()


