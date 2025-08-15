import tkinter as tk
from PIL import Image, ImageTk
import quizmodule

class QuestionTemplate():
    def __init__(self, window, questionNumber:int,  questionTitle:str, questionOptions:list, correctOption):
        window2 = tk.Toplevel(window)
        window2.withdraw()
        self.__questionTitle = questionTitle
        self.__questionOptions = questionOptions
        self.__tkinterWindow = window2
        self.__questionNumber = questionNumber
        self.__correctOption = correctOption
    def createQuestionWindow(self):
        self.__tkinterWindow.deiconify()
        popup = tk.Label(self.__tkinterWindow)
        popup.grid(sticky="s")
        def checkIfCorrect(optionButton):
            if optionButton.cget("text") == self.__correctOption:
                popup.config(text="correct!!!", font=("Arial", 20), fg="#0FB800")
            else:
                popup.config(text=f"wrong!!! its {self.__correctOption}", font=("Arial", 20), fg="#B80000")
        tk_questionTitle = tk.Label(self.__tkinterWindow, text=f"Question {self.__questionNumber}: {self.__questionTitle}", font=("Arial", 36, "italic"), wraplength=500)
        tk_questionTitle.grid(
            rowspan=10,
            columnspan=10,
            row=1,
            column=0
        )
        tk_questionOptions = []
        for i in self.__questionOptions:
            button = tk.Button(self.__tkinterWindow, text=f"{i}", font=("Arial", 16))
            button.config(command=checkIfCorrect(optionButton=button))
            tk_questionOptions.append(button)
        
        for i in range (0, len(tk_questionOptions)):
            tk_questionOptions[i].grid(
                row=7,
                column=i
            )
    def configInfo(self, quizImage, quizInfo, label, PIL, button, buttoncommand):
        if not PIL == None:
            labelImage = ImageTk.PhotoImage(quizImage)
        else:
            labelImage = tk.PhotoImage(file=quizImage)
        label.image=labelImage
        label.config(
            text=quizInfo,
            font=("Arial", 16), 
            wraplength=500, 
            image=labelImage,
            justify="left", 
            compound="right",
            anchor="e"
            )
        label.image=labelImage
        label.grid(columnspan=2, column=1)
        button.config(command=buttoncommand)


