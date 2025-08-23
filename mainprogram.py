import quizmodule
import tkinter as tk
from PIL import Image, ImageTk
from pygame import mixer
import layerimage
import os
import tkinter.font as tkFont

mixer.init()
root = tk.Tk()
class Menu:
    #Loading main menu music
    mixer.music.load("audio/Pookatori and Friends.mp3")
    mixer.music.play(-1,0.0)

    def __init__(self, quizzes, root):
    #Destroying the Welcome Page widgets
        for widget in root.winfo_children():
            widget.destroy()
        root.title("Quiz Menu")
        root.geometry("1440x1024")
    #Creating image references
        quizWidgets = []
        self.images = []
        canvas = tk.Canvas(root, width=1420, height=1200)
        buttonSFX = mixer.Sound("audio/button.mp3")
        canvas.grid()
    #Button sound
        def onClick(event):
            buttonSFX.play()
        for i in range(0, len(quizzes)):
            #Retrieving and resizing the image used for the quizzes
            quizWidgetImage = Image.open(f"{quizzes[i].getImage()}")
            quizWidgetImage = quizmodule.Quiz.resizeImg(200, quizWidgetImage)
            quizWidgetImage = ImageTk.PhotoImage(quizWidgetImage)
            title = quizzes[i].getTitle()
            file = quizzes[i].getFile()

            def runQuiz(file=file):
                quiz = quizmodule.Quiz(file)
                quiz.run()
            #Creating the buttons for each quiz 
            quizWidget = tk.Button(
                canvas,
                text=title,
                image=quizWidgetImage, 
                compound="bottom", 
                font=("Chalkboard", 16, "italic"), 
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
        
        canvas.create_text(1420/2-500, 100, text="Choose your challenge:", font=tkFont.Font(family="Marker Felt", size=64, weight="bold"), fill="#141615", width=450, anchor="nw")
        
        def avatar():
            #--- CRIMSON ---
            crimsonwindow = tk.Toplevel(root)
            crimsonwindow.title("Crimson Avatar")
            crimsonwindow.image_refs = []  # Store image references
            
            crimsonImages = []
            for image in sorted(os.listdir("images/crimson")):
                if not image.startswith('.'):  # Skip non image files
                    crimsonImages.append(f"images/crimson/{image}")
            
            # Create canvas for crimson
            crimson_canvas = tk.Canvas(crimsonwindow, width=400, height=400, bg="#FFA1A1")
            crimson_canvas.grid(row=0, column=6, rowspan=6, padx=10, pady=10)
            
            # Creating the crimson avatar
            crimsonAvatar = layerimage.Avatars(crimsonImages, "crimson_attributes.json", crimsonwindow, canvas=crimson_canvas)
            crimson_imglist = []
            #Resizing all layers 
            for image in crimsonAvatar.getImages():
                img = crimsonAvatar.resizeImg(200, image)
                crimson_imglist.append(img)
                crimsonwindow.image_refs.append(img)  # Store reference
            
            crimsonAvatar.setImages(crimson_imglist)
            crimsonAvatar.create_Buttons()
            #Creates avatar
            crimsonAvatar.activateAvatar(200, 200)
            #--- COBALT ---
            # Create Cobalt avatar window
            cobaltwindow = tk.Toplevel(root)
            cobaltwindow.title("Cobalt Avatar")
            cobaltwindow.image_refs = []  # Store image references
                        
            cobaltImages = []
            for image in sorted(os.listdir("images/cobalt")):
                if not image.startswith('.'):  # Skip non image files
                    cobaltImages.append(f"images/cobalt/{image}")
                        
            # Create canvas for cobalt
            cobalt_canvas = tk.Canvas(cobaltwindow, width=400, height=400, bg="#A1E3FF")
            cobalt_canvas.grid(row=0, column=6, rowspan=6, padx=10, pady=10)
                        
            # Create the cobalt avatar
            cobaltAvatar = layerimage.Avatars(cobaltImages, "cobalt_attributes.json", cobaltwindow, canvas=cobalt_canvas)
            cobalt_imglist = []
            #Resizing all layers 
            for image in cobaltAvatar.getImages():
                img = cobaltAvatar.resizeImg(600, image)
                cobalt_imglist.append(img)
                cobaltwindow.image_refs.append(img)  # Store reference
                        
            cobaltAvatar.setImages(cobalt_imglist)
            cobaltAvatar.create_Buttons()
            #Creates avatar
            cobaltAvatar.activateAvatar(200, 200)
            

        avatarimg = Image.open("images/avatarcustomisation.png")
        avatarimg = quizmodule.Quiz.resizeImg(300, avatarimg)
        avatar_tk = ImageTk.PhotoImage(avatarimg)
        avatarbutton = tk.Button(text="Customise your Avatar", font=tkFont.Font(family="Chalkboard", size=24), fg="#1A2178", command=avatar, image=avatar_tk, compound="bottom")
        avatarbutton.image = avatar_tk 
        quitbutton = tk.Button(text="Quit", command=quit, font=tk.font.Font(family="Chalkboard", size=16), fg="#870F29")
        def go_back():
        # Code to "return" to welcome screen (changing all the widgets to the welcome screen ones)
            self.welcome()
        backbutton = tk.Button(text="Back", command=go_back, font=tk.font.Font(family="Chalkboard", size=16), fg="#085C80")
        canvas.create_window(350, 600, window=avatarbutton)
        canvas.create_window(50, 50, window=quitbutton)
        canvas.create_window(150, 50, window=backbutton)
        root.mainloop()
    @staticmethod
    def welcome():
    #Welcome screen (in the class so that init can easily call it)
        for widget in root.winfo_children(): #Clearing the screen
            widget.destroy()
        root.title("Welcome")
        title_font = tkFont.Font(family="Phosphate", size=72, weight="bold")
        subtitle_font = tkFont.Font(family="Noteworthy", size=36, slant="italic")

        canvas = tk.Canvas(root, width=1420, height=1200)
        canvas.grid()

        bg_img = Image.open("images/welcomebg.png")
        #Resize background image to fit the dimensions of the canvas
        bg_img = quizmodule.Quiz.resizeImg(1420, bg_img)  
        bg_imgtk = ImageTk.PhotoImage(bg_img)
        #Keep background images
        canvas.bg_imgtk = bg_imgtk
        canvas.create_image(0, 0, image=bg_imgtk, anchor="nw")


        q_whatColourIsThat = quizmodule.Quiz("whatColourIsThat.json")
        q_allAboutHSV = quizmodule.Quiz("allAboutHSV.json")
        q_colourRelationships = quizmodule.Quiz("colourRelationships.json")
        q_tiersOfColours = quizmodule.Quiz("tiersOfColours.json")

        def menu():
            Menu([q_allAboutHSV, q_whatColourIsThat, q_colourRelationships, q_tiersOfColours], root=root)

        #Button for initialising menu
        menubutton = tk.Button(text="Begin the Crusade", fg="#5E0083", font=tk.font.Font(family="Chalkboard", size=24), command=menu)
        #Title/subtitle
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
                #--- CRIMSON ---
        crimsonbg = Image.open("images/crimsonmenu.png")
        cobaltbg = Image.open("images/cobaltmenu.png")
        crimsonbg = quizmodule.Quiz.resizeImg(300, crimsonbg)
        crimsonbg = ImageTk.PhotoImage(crimsonbg)
        cobaltbg = quizmodule.Quiz.resizeImg(300, cobaltbg)
        cobaltbg = ImageTk.PhotoImage(cobaltbg)
        # Add the transparent background to both canvases

        crimsonwindow = root
        crimsonwindow.image_refs = []  # Store image references
        crimson_canvas = tk.Canvas(root, width=300, height=324)
        crimson_canvas.place(x=50, y=500)
        
        crimson_canvas.create_image(0, 0, image=crimsonbg, anchor="nw")
        root.transparent_crimson = crimsonbg

        crimsonImages = []
        for image in sorted(os.listdir("images/crimson")):
            if not image.startswith('.'):  # Skip non image files
                crimsonImages.append(f"images/crimson/{image}")
        
        # Creating the crimson avatar
        crimsonAvatar = layerimage.Avatars(crimsonImages, "crimson_attributes.json", crimsonwindow, canvas=crimson_canvas)
        crimson_imglist = []
        #Resizing all layers 
        for image in crimsonAvatar.getImages():
            img = crimsonAvatar.resizeImg(200, image)
            crimson_imglist.append(img)
            crimsonwindow.image_refs.append(img)  # Store reference
        
        crimsonAvatar.setImages(crimson_imglist)
        #Creates avatar
        crimsonAvatar.activateAvatar(150, 200)
        #--- COBALT ---
        # Create Cobalt avatar window
        cobaltwindow = root
        cobaltwindow.image_refs = []  # Store image references
        cobalt_canvas = tk.Canvas(root, width=300, height=324)
        cobalt_canvas.place(x=1050, y=500)
        cobalt_canvas.create_image(0, 0, image=cobaltbg, anchor="nw")
        root.transparent_cobalt = cobaltbg

        cobaltImages = []
        for image in sorted(os.listdir("images/cobalt")):
            if not image.startswith('.'):  # Skip non image files
                cobaltImages.append(f"images/cobalt/{image}")
                    
        # Create the cobalt avatar
        cobaltAvatar = layerimage.Avatars(cobaltImages, "cobalt_attributes.json", cobaltwindow, canvas=cobalt_canvas)
        cobalt_imglist = []
        #Resizing all layers 
        for image in cobaltAvatar.getImages():
            img = cobaltAvatar.resizeImg(600, image)
            cobalt_imglist.append(img)
            cobaltwindow.image_refs.append(img)  # Store reference
                    
        cobaltAvatar.setImages(cobalt_imglist)
        #Creates avatar
        cobaltAvatar.activateAvatar(150, 200)

#Starting the program
Menu.welcome()
root.mainloop()


