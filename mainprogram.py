import quizmodule
import tkinter as tk
from PIL import Image, ImageTk
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
            
        # columnNum=1
        # rowNum=1
        # def motion(event):
        #     crimson = ImageTk.PhotoImage(quizmodule.Quiz.resizeImg(10, "images/crimson/crimson.png"))
            # crimson.pack(x=event.x, y=event.y)
        #     canvas.create_image(event.x(), event.y(), image=crimson, anchor="nw")
        # root.bind("<Motion>", motion)
            # window.after(100, dante_jumpscare.place(x=event.x-10, y=event.y-10))
            # window.after(100, dante_jumpscare.place(x=event.x-100, y=event.y-100))
            # window.after(100, dante_jumpscare.place(x=event.x-1000, y=event.y-1000))

        # for i, j in (quizWidgets), range(0, len(quizWidgets)):
        #     #0 0
        #     # 208 1
        #     # 0 237
        #     # 208 238
        
        #     canvas.create_window(coordinates[j][0], coordinates[j][1], i)
            # i.grid(
            #     row=rowNum, 
            #     column=columnNum,
            # )
            # columnNum +=1
            # if columnNum>2:
            #     rowNum+=1
            #     columnNum=1
        
        def debug():
            for i in (quizWidgets):
                print(i.winfo_x(), i.winfo_y())
        root.after(100, debug)
            

        root.mainloop()
    

root = tk.Tk()
root.title("Welcome")

canvas = tk.Canvas(root, width=1420, height=1200)

canvas.grid()


bg_img = Image.open("images/welcomebg.png")
bg_img = quizmodule.Quiz.resizeImg(1420, bg_img)  
bg_imgtk = ImageTk.PhotoImage(bg_img)
canvas.create_image(0, 0, image=bg_imgtk, anchor="nw")
canvas.bg_imgtk = bg_imgtk

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



q_whatColourIsThat = quizmodule.Quiz("whatColourIsThat.json")
q_allAboutHSV = quizmodule.Quiz("allAboutHSV.json")
q_colourRelationships = quizmodule.Quiz("colourRelationships.json")
q_tiersOfColours = quizmodule.Quiz("tiersOfColours.json")



# if menu == "whatColourIsThat.json":
#     q_whatColourIsThat.run()

# if menu == "allAboutHSV.json":
# q_allAboutHSV.run()

root.mainloop()


