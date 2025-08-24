import quizmodule
import tkinter as tk
from PIL import Image, ImageTk
from pygame import mixer
import layerimage
import os
import tkinter.font as tkFont

# Initialize pygame mixer for sound effects and music
mixer.init()
# Create the main application window
root = tk.Tk()

class Menu:
    # Load main menu music 
    mixer.music.load("audio/Pookatori and Friends.mp3")
    mixer.music.play(-1,0.0)  # -1 means loop indefinitely, 0.0 means start from beginning

    def __init__(self, quizzes, root):
        # Constructor for the Menu class - creates the main quiz selection screen
        self.root = root
        # Destroying the Welcome Page widgets to start fresh
        for widget in root.winfo_children():
            widget.destroy()
        self.root.title("Quiz Menu")
        self.root.geometry("1440x1024")
        
        # Creating image references list to prevent garbage collection
        quizWidgets = []  # Store quiz buttons
        self.images = []  # Store PhotoImage references
        # Create main canvas for the menu
        canvas = tk.Canvas(self.root, width=1420, height=1200)
        # Sound effect for button clicks
        buttonSFX = mixer.Sound("audio/button.mp3")
        canvas.grid()
        
        # Button sound effect handler
        def onClick(event):
            buttonSFX.play()
            
        # Create buttons for each available quiz
        for i in range(0, len(quizzes)):
            # Retrieve and resize the image used for the quizzes
            quizWidgetImage = Image.open(f"{quizzes[i].getImage()}")
            quizWidgetImage = quizmodule.Quiz.resizeImg(200, quizWidgetImage)
            quizWidgetImage = ImageTk.PhotoImage(quizWidgetImage)
            title = quizzes[i].getTitle()
            file = quizzes[i].getFile()

            # Function to launch the selected quiz
            def runQuiz(file=file):
                quiz = quizmodule.Quiz(file)
                quiz.run()
                
            # Creating the buttons for each quiz with an image and text
            quizWidget = tk.Button(
                canvas,
                text=title,
                image=quizWidgetImage, 
                compound="bottom",  
                font=("Chalkboard", 16, "italic"), 
                wraplength="200",  
                command=runQuiz)
            # Store image reference to prevent garbage collection
            self.images.append(quizWidgetImage)
            # Attach sound effect to button click
            quizWidget.bind("<Button-1>", onClick)
            quizWidgets.append(quizWidget)

        # Define grid positions for quiz buttons (2x2 grid)
        coordinates = [[1420/2+100, 100], [1420/2+100, 400], [1420/2+400, 100], [1420/2+400, 400]]

        # Load and display the background image
        bg_img = Image.open("images/menubg.png")
        bg_img = quizmodule.Quiz.resizeImg(1420, bg_img)  
        bg_imgtk = ImageTk.PhotoImage(bg_img)
        canvas.create_image(0, 0, image=bg_imgtk, anchor="nw")
        canvas.bg_imgtk = bg_imgtk  # Store reference to prevent garbage collection

        # Place quiz buttons on the canvas at defined coordinates
        for widgetNum, widget in enumerate(quizWidgets):
            canvas.create_window(coordinates[widgetNum][0], coordinates[widgetNum][1], anchor="nw", window=widget)
        
        # Add title text to the menu
        canvas.create_text(1420/2-500, 100, text="Choose your challenge:", font=tkFont.Font(family="Marker Felt", size=64, weight="bold"), fill="#141615", width=450, anchor="nw")
        
        # Avatar customization function - opens separate windows for each character
        def avatar():
            #--- CRIMSON CHARACTER ---
            # Create a new window for Crimson avatar customization
            crimsonwindow = tk.Toplevel(self.root)
            crimsonwindow.title("Crimson Avatar")
            crimsonwindow.image_refs = []  # Store image references to prevent garbage collection
            
            # Load all Crimson character component images
            crimsonImages = []
            for image in sorted(os.listdir("images/crimson")):
                if not image.startswith('.'):  # Skip hidden files (like .DS_Store)
                    crimsonImages.append(f"images/crimson/{image}")
            
            # Create canvas for Crimson avatar display
            crimson_canvas = tk.Canvas(crimsonwindow, width=400, height=400, bg="#FFA1A1")
            crimson_canvas.grid(row=0, column=6, rowspan=6, padx=10, pady=10)
            
            # Initialize the Crimson avatar system
            crimsonAvatar = layerimage.Avatars(crimsonImages, "crimson_attributes.json", crimsonwindow, canvas=crimson_canvas)
            crimson_imglist = []
            # Resize all layer images to fit properly
            for image in crimsonAvatar.getImages():
                img = crimsonAvatar.resizeImg(200, image)
                crimson_imglist.append(img)
                crimsonwindow.image_refs.append(img)  # Store reference to prevent garbage collection
            
            # Set the resized images and create UI elements
            crimsonAvatar.setImages(crimson_imglist)
            crimsonAvatar.create_Buttons()
            # Display the avatar at the center of the canvas
            crimsonAvatar.activateAvatar(200, 200)
            
            #--- COBALT CHARACTER ---
            # Create a new window for Cobalt avatar customization
            cobaltwindow = tk.Toplevel(self.root)
            cobaltwindow.title("Cobalt Avatar")
            cobaltwindow.image_refs = []  # Store image references to prevent garbage collection
                        
            # Load all Cobalt character component images
            cobaltImages = []
            for image in sorted(os.listdir("images/cobalt")):
                if not image.startswith('.'):  # Skip hidden files
                    cobaltImages.append(f"images/cobalt/{image}")
                        
            # Create canvas for Cobalt avatar display
            cobalt_canvas = tk.Canvas(cobaltwindow, width=400, height=400, bg="#A1E3FF")
            cobalt_canvas.grid(row=0, column=6, rowspan=6, padx=10, pady=10)
                        
            # Initialize the Cobalt avatar system
            cobaltAvatar = layerimage.Avatars(cobaltImages, "cobalt_attributes.json", cobaltwindow, canvas=cobalt_canvas)
            cobalt_imglist = []
            # Resize all layer images to fit properly
            for image in cobaltAvatar.getImages():
                img = cobaltAvatar.resizeImg(600, image)  
                cobalt_imglist.append(img)
                cobaltwindow.image_refs.append(img)  # Store reference to prevent garbage collection
                        
            # Set the resized images and create UI elements
            cobaltAvatar.setImages(cobalt_imglist)
            cobaltAvatar.create_Buttons()
            # Display the avatar at the center of the canvas
            cobaltAvatar.activateAvatar(200, 200)
            
        # Load avatar customization button image and create the button
        avatarimg = Image.open("images/avatarcustomisation.png")
        avatarimg = quizmodule.Quiz.resizeImg(300, avatarimg)
        avatar_tk = ImageTk.PhotoImage(avatarimg)
        avatarbutton = tk.Button(text="Customise your Avatar", font=tkFont.Font(family="Chalkboard", size=24), fg="#1A2178", command=avatar, image=avatar_tk, compound="bottom")
        avatarbutton.image = avatar_tk  # Store reference to prevent garbage collection
        
        # Quit button to exit application
        quitbutton = tk.Button(text="Quit", command=quit, font=tk.font.Font(family="Chalkboard", size=16), fg="#870F29")
        
        # Function to return to welcome screen
        def go_back():
            # Reset to welcome screen by recreating all welcome screen elements
            self.welcome()
            
        # Back button to return to welcome screen
        backbutton = tk.Button(text="Back", command=go_back, font=tk.font.Font(family="Chalkboard", size=16), fg="#085C80")
        
        def info():
            self.info("crimsoncobalt.txt")

        infobutton = tk.Button(text="Info", command=info, font=tk.font.Font(family="Chalkboard", size=16), fg="#088022")

        # Place buttons on the canvas
        canvas.create_window(350, 600, window=avatarbutton)
        canvas.create_window(50, 50, window=quitbutton)
        canvas.create_window(150, 50, window=backbutton)
        canvas.create_window(250, 50, window=infobutton)        
        # Start the main event loop
        self.root.mainloop()
        
    @staticmethod
    def welcome():
        # Static method to create the welcome screen
        
        # Clearing the screen of any existing widgets
        for widget in root.winfo_children(): 
            widget.destroy()
            
        # Set window title and prepare fonts
        root.title("Welcome")
        title_font = tkFont.Font(family="Phosphate", size=72, weight="bold")
        subtitle_font = tkFont.Font(family="Noteworthy", size=36, slant="italic")

        # Create canvas for welcome screen
        canvas = tk.Canvas(root, width=1420, height=1200)
        canvas.grid()

        # Load and display background image
        bg_img = Image.open("images/welcomebg.png")
        # Resize background image to fit the dimensions of the canvas
        bg_img = quizmodule.Quiz.resizeImg(1420, bg_img)  
        bg_imgtk = ImageTk.PhotoImage(bg_img)
        # Store background image reference to prevent garbage collection
        canvas.bg_imgtk = bg_imgtk
        canvas.create_image(0, 0, image=bg_imgtk, anchor="nw")

        # Initialize all available quizzes
        q_whatColourIsThat = quizmodule.Quiz("whatColourIsThat.json")
        q_allAboutHSV = quizmodule.Quiz("allAboutHSV.json")
        q_colourRelationships = quizmodule.Quiz("colourRelationships.json")
        q_tiersOfColours = quizmodule.Quiz("tiersOfColours.json")

        # Function to transition to the main menu screen
        def menu():
            Menu([q_allAboutHSV, q_whatColourIsThat, q_colourRelationships, q_tiersOfColours], root=root)

        # Button to start the application and go to menu
        menubutton = tk.Button(text="Begin the Crusade", fg="#5E0083", font=tk.font.Font(family="Chalkboard", size=24), command=menu)
        
        # Add title and subtitle text to welcome screen
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
        # Add start button to canvas
        canvas.create_window(
            1420/2,
            700,
            window=menubutton)
            
        #--- WELCOME SCREEN AVATAR DISPLAYS ---
        
        # Load character background images
        crimsonbg = Image.open("images/crimsonmenu.png")
        cobaltbg = Image.open("images/cobaltmenu.png")
        # Resize backgrounds and convert to PhotoImage
        crimsonbg = quizmodule.Quiz.resizeImg(300, crimsonbg)
        width1, height1 = crimsonbg.size
        crimsonbg = ImageTk.PhotoImage(crimsonbg)
        cobaltbg = quizmodule.Quiz.resizeImg(300, cobaltbg)
        width2, height2 = cobaltbg.size
        cobaltbg = ImageTk.PhotoImage(cobaltbg)

        # Setup Crimson character display on welcome screen
        crimsonwindow = root
        crimsonwindow.image_refs = []  # Store image references to prevent garbage collection

        # Create canvas for Crimson character
        crimson_canvas = tk.Canvas(root, width=width1, height=height1)
        crimson_canvas.place(x=50, y=500)  # Position on the left side
        
        # Display Crimson background
        crimson_canvas.create_image(0, 0, image=crimsonbg, anchor="nw")
        root.transparent_crimson = crimsonbg  # Store reference to prevent garbage collection

        # Load Crimson character component images
        crimsonImages = []
        for image in sorted(os.listdir("images/crimson")):
            if not image.startswith('.'):  # Skip hidden files
                crimsonImages.append(f"images/crimson/{image}")
        
        # Initialize Crimson avatar for welcome screen
        crimsonAvatar = layerimage.Avatars(crimsonImages, "crimson_attributes.json", crimsonwindow, canvas=crimson_canvas)
        crimson_imglist = []
        # Resize all layers to fit the welcome screen display
        for image in crimsonAvatar.getImages():
            img = crimsonAvatar.resizeImg(200, image)
            crimson_imglist.append(img)
            crimsonwindow.image_refs.append(img)  # Store reference to prevent garbage collection
        
        # Apply the resized images and display the avatar
        crimsonAvatar.setImages(crimson_imglist)
        crimsonAvatar.activateAvatar(150, 200)  # Position centered on the canvas
        
        #--- COBALT WELCOME SCREEN DISPLAY ---
        # Setup Cobalt character display on welcome screen
        cobaltwindow = root
        cobaltwindow.image_refs = []  # Store image references to prevent garbage collection

        # Create canvas for Cobalt character
        cobalt_canvas = tk.Canvas(root, width=width2, height=height2)
        cobalt_canvas.place(x=1050, y=500)  # Position on the right side
        
        # Display Cobalt background
        cobalt_canvas.create_image(0, 0, image=cobaltbg, anchor="nw")
        root.transparent_cobalt = cobaltbg  # Store reference to prevent garbage collection

        # Load Cobalt character component images
        cobaltImages = []
        for image in sorted(os.listdir("images/cobalt")):
            if not image.startswith('.'):  # Skip hidden files
                cobaltImages.append(f"images/cobalt/{image}")
                    
        # Initialize Cobalt avatar for welcome screen
        cobaltAvatar = layerimage.Avatars(cobaltImages, "cobalt_attributes.json", cobaltwindow, canvas=cobalt_canvas)
        cobalt_imglist = []
        # Resize all layers to fit the welcome screen display
        for image in cobaltAvatar.getImages():
            img = cobaltAvatar.resizeImg(200, image)  # Changed from 600 to 200 for consistency
            cobalt_imglist.append(img)
            cobaltwindow.image_refs.append(img)  # Store reference to prevent garbage collection
                    
        # Apply the resized images and display the avatar
        cobaltAvatar.setImages(cobalt_imglist)
        cobaltAvatar.activateAvatar(150, 200)  # Position centered on the canvas
    def info(self, infofile):
        # Create a new top-level window for displaying info
        image = Image.open("images/crimco.png")
        image = quizmodule.Quiz.resizeImg(335, image)
        image = ImageTk.PhotoImage(image)
        window = tk.Toplevel(self.root)
        window.geometry("500x500")  # Set window size
        window.title("Game Information")

        # Create a canvas to hold the label and set its background color
        windowcanvas = tk.Canvas(window, width=500, height=500, bg="#ECDCFF")
        windowcanvas.pack(fill="both", expand=True)
        # Read the info text from the provided file
        with open(infofile, "r") as file:
            gameinfo = file.read()

        # Place the info label onto the canvas at position (300, 300)
        windowcanvas.create_text(250, 250, text=gameinfo, fill="#5F0FA0", font=tkFont.Font(family='Chalkboard', size=10), width=450, justify="center")
        close_btn = tk.Button(window, text="Close", command=window.destroy, font=tkFont.Font(family='Chalkboard') )
        windowcanvas.create_image(250, 100, image=image)
        windowcanvas.create_window(250, 450, window=close_btn)

        windowcanvas.image = image
        
        

# Start the application by showing the welcome screen
Menu.welcome()
# Start the main event loop
root.mainloop()


