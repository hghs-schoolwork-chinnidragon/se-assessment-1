import quizmodule
import tkinter as tk
from PIL import Image, ImageTk
class Menu:
    # @staticmethod
    # def createwindow():
    #     window = tk.Tk()

    def __init__(self, quizzes):
        window = tk.Tk()
        window.geometry("1440x1024")
        quizWidgets = []
        for i in range(0, len(quizzes)):
            quizWidgetImage = Image.open(f"{quizzes[i].getImage()}")
            quizWidgetImage = quizWidgetImage.resize((round(quizWidgetImage.width/4), round(quizWidgetImage.height/4)))
            quizWidgetImage = ImageTk.PhotoImage(quizWidgetImage)
            t = quizzes[i].getTitle()
            #need to resize images
            def onClick():
                return t
            quizWidget = tk.Button(window, text=f"{t}", image=f"{quizWidgetImage}", compound="bottom", font=("Arial", 36), wraplength="500", command=onClick)
            quizWidgets.append(quizWidget)
            
        for i in (quizWidgets):
            for j in range(2, 8):
                i.grid(
                    row=j,
                    column=j
                )

        window.mainloop()
    


q_whatColourIsThat = quizmodule.Quiz("whatColourIsThat.json")
q_allAboutHSV = quizmodule.Quiz("allAboutHSV.json")

# menu = Menu([q_allAboutHSV, q_whatColourIsThat])
# if menu == "whatColourIsThat.json":
q_whatColourIsThat.run()

# if menu == "allAboutHSV.json":
q_allAboutHSV.run()


