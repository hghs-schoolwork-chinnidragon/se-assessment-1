import tkinter as tk
from PIL import Image, ImageTk
from quizmodule import Quiz

class QuestionTemplate():
    def __init__(self, tkinterwindow,  questionTitle, questionOptions):
        self.__questionTitle = questionTitle
        self.__questionOptions = questionOptions
        self.__tkinterWindow = tkinterwindow
    def createQuestionWindow(self):
        tk_questionTitle = tk.Label(self.__tkinterWindow, text=f"{self.__questionTitle}", font=("Arial", 60), wraplength=1420)
        tk_questionTitle.grid(
            row=1,
            column=2
        )
        tk_questionOptions = []
        for i in self.__questionOptions:
            tk_questionOptions.append(tk.Label(self.__tkinterWindow, text=f"{self.__questionOptions[i]}", font=("Arial", 24)))
        
        for i in range (0, len(tk_questionOptions)):
            tk_questionOptions[i].grid(
                row=5,
                column=i
            )
            
    def configInfo(quizImage, quizInfo, label):
            labelImage = tk.PhotoImage(file=quizImage)
            label.config(text=quizInfo, font=("Arial", 24), wraplength=1440/2, anchor="e", justify="left", image=labelImage, compound="left" )
            label.grid()

        
