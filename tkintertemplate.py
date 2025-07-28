import tkinter as tk
from PIL import Image, ImageTk
from quiz import Quiz

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
        tk_questionOptions = tk.Label()
    def configInfo(quizImage, quizInfo, label):
            labelImage = tk.PhotoImage(file=quizImage)
            label.config(text=quizInfo, font=("Arial", 24), wraplength=1440/2, anchor="e", justify="left", image=labelImage, compound="left" )
            label.pack()

        
