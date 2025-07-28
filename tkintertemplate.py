import tkinter as tk
from PIL import Image, ImageTk
from quiz import Quiz

class QuestionTemplate(Quiz):
    def __init__(self):
        pass
    def createQuestionWindow(self):
        tk_questionTitle = tk.Label(window, text=f"{self.__questions}"Aria)
        
