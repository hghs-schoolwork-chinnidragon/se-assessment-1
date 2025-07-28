import tkinter as tk
from PIL import Image, ImageTk
from quiz import Quiz

class QuestionTemplate():
    def __init__(self, tkinterwindow,  questionTitle, questionOptions):
        self.__questionTitle = questionTitle
        self.__questionOptions = questionOptions
        self.__tkinterWindow = tkinterwindow
    def createQuestionWindow(self):
        tk_questionTitle = tk.Label(self.__tkinterwindow, text=f"{self.__questionTitle}", font=("Arial", 60))
        tk_questionTitle.grid()

        
