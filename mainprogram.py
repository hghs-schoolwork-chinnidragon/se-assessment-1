import quizmodule
import tkinter as tk
from PIL import Image, ImageTk
class Menu:
    # @staticmethod
    # def createwindow():
    #     window = tk.Tk()

    def __init__(self, quizzes):
        window = tk.Toplevel()
        window.title("Quiz Menu")
        window.geometry("1440x1024")
        quizWidgets = []
        self.images = []
        for i in range(0, len(quizzes)):
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
                window,
                text=title,
                image=quizWidgetImage, 
                compound="bottom", 
                font=("Arial", 16, "italic"), 
                wraplength="200", 
                command=runQuiz)
            self.images.append(quizWidgetImage)
            print(self.images)
            quizWidgets.append(quizWidget)
            
        columnNum=1
        rowNum=1
        for i in (quizWidgets):
            i.grid(
                row=rowNum, 
                column=columnNum,
            )
            columnNum +=1
            if columnNum>2:
                rowNum+=1
                columnNum=1

        window.mainloop()
    

root = tk.Tk()
root.title("Welcome")

canvas = tk.Canvas(root, width=1420, height=1200)

canvas.grid()


bg_img = Image.open("images/wlecomebg2.png")
bg_img = quizmodule.Quiz.resizeImg(1420, bg_img)  
bg_imgtk = ImageTk.PhotoImage(bg_img)
canvas.create_image(0, 0, image=bg_imgtk, anchor="nw")
canvas.bg_imgtk = bg_imgtk

def menu():
    Menu([q_allAboutHSV, q_whatColourIsThat, q_colourRelationships, q_tiersOfColours])

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



q_whatColourIsThat = quizmodule.Quiz("whatColourIsThat.json")
q_allAboutHSV = quizmodule.Quiz("allAboutHSV.json")
q_colourRelationships = quizmodule.Quiz("colourRelationships.json")
q_tiersOfColours = quizmodule.Quiz("tiersOfColours.json")



# if menu == "whatColourIsThat.json":
#     q_whatColourIsThat.run()

# if menu == "allAboutHSV.json":
# q_allAboutHSV.run()

root.mainloop()


