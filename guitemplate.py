import tkinter as tk
from PIL import Image, ImageTk
import quizmodule

class QuestionTemplate():
    def __init__(self, tkinterwindow, questionNumber:int,  questionTitle:str, questionOptions:list, correctOption):
        self.__questionTitle = questionTitle
        self.__questionOptions = questionOptions
        self.__tkinterWindow = tkinterwindow
        self.__questionNumber = questionNumber
        self.__correctOption = correctOption
    def createQuestionWindow(self):
        popup = tk.Label(self.__tkinterWindow)
        popup.grid(sticky="s")
        def checkIfCorrect(optionButton):
            if optionButton.cget("text") == self.__correctOption:
                popup.config(self.__tkinterWindow, text="correct!!!", font=("arial", 20), fg="#0FB800")
            else:
                popup.config(self.__tkinterWindow, text=f"wrong!!! its {self.__correctOption}", font=("arial", 20), fg="#B80000")
        tk_questionTitle = tk.Label(self.__tkinterWindow, text=f"Question {self.__questionNumber}: {self.__questionTitle}", font=("Arial", 60), wraplength=1420)
        tk_questionTitle.grid(
            row=1,
            column=2
        )
        tk_questionOptions = []
        for i in self.__questionOptions:
            tk_questionOptions.append(tk.Button(self.__tkinterWindow, text=f"{i}", font=("Arial", 24), command=checkIfCorrect))
        
        for i in range (0, len(tk_questionOptions)):
            tk_questionOptions[i].grid(
                row=5,
                column=i
            )
            
    def configInfo(quizImage, quizInfo, label, PIL):
            if not PIL == None:
                labelImage = ImageTk.PhotoImage(quizImage)
            else:
                labelImage = tk.PhotoImage(file=quizImage)
            label.image=labelImage
            label.config(text=quizInfo, font=("Arial", 10), wraplength=1440, image=labelImage, compound="right")
            label.image=labelImage
            label.grid(columnspan=2, column=1)

