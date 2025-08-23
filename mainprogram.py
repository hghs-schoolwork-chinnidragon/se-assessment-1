import quizmodule
import tkinter as tk
from PIL import Image, ImageTk
from pygame import mixer
import layerimage
import os
import tkinter.font as tkFont


mixer.init()

class Menu:
    # @staticmethod
    # def createwindow():
    #     window = tk.Tk()
    mixer.music.load("audio/Pookatori and Friends.mp3")
    mixer.music.play(-1,0.0)


    def __init__(self, quizzes, root):
        for widget in root.winfo_children():
            widget.destroy()
        root.title("Quiz Menu")
        root.geometry("1440x1024")
        quizWidgets = []
        self.images = []
        canvas = tk.Canvas(root, width=1420, height=1200)
        buttonSFX = mixer.Sound("audio/button.mp3")
        
        canvas.grid()
        def onClick(event):
            buttonSFX.play()
        for i in range(0, len(quizzes)):
            quizWidgetImage = Image.open(f"{quizzes[i].getImage()}")
            quizWidgetImage = quizmodule.Quiz.resizeImg(200, quizWidgetImage)
            quizWidgetImage = ImageTk.PhotoImage(quizWidgetImage)
            title = quizzes[i].getTitle()
            file = quizzes[i].getFile()
            #need to resize images
            def runQuiz(file=file):
                quiz = quizmodule.Quiz(file)
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
            # Make sound on click
            quizWidget.bind("<Button-1>", onClick)
            quizWidgets.append(quizWidget)

        coordinates = [[1420/2+100, 100], [1420/2+100, 400], [1420/2+400, 100], [1420/2+400, 400]]

        bg_img = Image.open("images/menubg.png")
        bg_img = quizmodule.Quiz.resizeImg(1420, bg_img)  
        bg_imgtk = ImageTk.PhotoImage(bg_img)
        canvas.create_image(0, 0, image=bg_imgtk, anchor="nw")
        canvas.bg_imgtk = bg_imgtk

        for widgetNum, widget in enumerate(quizWidgets):
            canvas.create_window(coordinates[widgetNum][0], coordinates[widgetNum][1], anchor="nw", window=widget)
        
        canvas.create_text(1420/2-500, 100, text="Choose your challenge:", font=tkFont.Font(family="Comic Sans MS", size=64, weight="bold"), fill="#141615", width=450, anchor="nw")
        
        def avatar():
            #--- CRIMSON ---
            crimsonwindow = tk.Toplevel(root)
            crimsonwindow.title("Crimson Avatar")
            crimsonwindow.image_refs = []  # Store image references
            
            crimsonImages = []
            for image in sorted(os.listdir("images/crimson")):
                if not image.startswith('.'):  # Skip .DS_Store files
                    crimsonImages.append(f"images/crimson/{image}")
            
            # Creating canvas for crimson
            crimson_canvas = tk.Canvas(crimsonwindow, width=400, height=400, bg="#FFA1A1")
            crimson_canvas.grid(row=0, column=6, rowspan=6, padx=10, pady=10)
            
            # Creating the crimson avatar
            crimsonAvatar = layerimage.Avatars(crimsonImages, "crimson_attributes.json", crimsonwindow, canvas=crimson_canvas)
            crimson_imglist = []
            for image in crimsonAvatar.getImages():
                img = crimsonAvatar.resizeImg(200, image)
                crimson_imglist.append(img)
                crimsonwindow.image_refs.append(img)  # Store reference
            
            crimsonAvatar.setImages(crimson_imglist)
            
            crimsonAvatar.create_Buttons()
            crimsonAvatar.activateAvatar()
            # Creating Cobalt avatar window
            cobaltwindow = tk.Toplevel(root)
            cobaltwindow.title("Cobalt Avatar")
            cobaltwindow.image_refs = []  # Store image references
                        
            cobaltImages = []
            for image in sorted(os.listdir("images/cobalt")):
                if not image.startswith('.'):  # Skip .DS_Store files
                    cobaltImages.append(f"images/cobalt/{image}")
                        
            # Creating canvas for cobalt
            cobalt_canvas = tk.Canvas(cobaltwindow, width=400, height=400, bg="#A1E3FF")
            cobalt_canvas.grid(row=0, column=6, rowspan=6, padx=10, pady=10)
                        
            # Creating the cobalt avatar
            cobaltAvatar = layerimage.Avatars(cobaltImages, "cobalt_attributes.json", cobaltwindow, canvas=cobalt_canvas)
            cobalt_imglist = []
            for image in cobaltAvatar.getImages():
                img = cobaltAvatar.resizeImg(750, image)
                cobalt_imglist.append(img)
                cobaltwindow.image_refs.append(img)  # Store reference
                        
            cobaltAvatar.setImages(cobalt_imglist)
                        
            cobaltAvatar.create_Buttons()
            cobaltAvatar.activateAvatar()
            

        avatarimg = Image.open("images/avatarcustomisation.png")
        avatarimg = quizmodule.Quiz.resizeImg(300, avatarimg)
        avatar_tk = ImageTk.PhotoImage(avatarimg)
        avatarbutton = tk.Button(text="customise avatar!!!", command=avatar, image=avatar_tk, compound="bottom")
        avatarbutton.image = avatar_tk 
        quitbutton = tk.Button(text="Quit", command=quit)
        def go_back():
            # Code to return to welcome screen
            pass
        backbutton = tk.Button(text="Back", command=go_back)
        canvas.create_window(400, 650, window=avatarbutton)
        canvas.create_window(50, 50, window=quitbutton)
        canvas.create_window(150, 50, window=backbutton)
        root.mainloop()
    

root = tk.Tk()
root.title("Welcome")
title_font = tkFont.Font(family="Comic Sans MS", size=72, weight="bold")
subtitle_font = tkFont.Font(family="Papyrus", size=36, slant="italic")

canvas = tk.Canvas(root, width=1420, height=1200)

canvas.grid()

bg_img = Image.open("images/welcomebg.png")
bg_img = quizmodule.Quiz.resizeImg(1420, bg_img)  
bg_imgtk = ImageTk.PhotoImage(bg_img)
canvas.bg_imgtk = bg_imgtk
canvas.create_image(0, 0, image=bg_imgtk, anchor="nw")


q_whatColourIsThat = quizmodule.Quiz("whatColourIsThat.json")
q_allAboutHSV = quizmodule.Quiz("allAboutHSV.json")
q_colourRelationships = quizmodule.Quiz("colourRelationships.json")
q_tiersOfColours = quizmodule.Quiz("tiersOfColours.json")

def menu():
    Menu([q_allAboutHSV, q_whatColourIsThat, q_colourRelationships, q_tiersOfColours], root=root)


menubutton = tk.Button(text="Begin the Crusade", fg="#15A702", bg="#15A702", command=menu)
canvas.create_text(
    1420/2, 300, 
    text="Welcome to....",
    font=subtitle_font, 
    fill="#141615"
    )
canvas.create_text(
    1420/2, 
    400, 
    text="Colour Crusaders", 
    font=title_font, 
    fill="#141615"
    )
canvas.create_window(
    1420/2,
    700,
    window=menubutton)
root.mainloop()


