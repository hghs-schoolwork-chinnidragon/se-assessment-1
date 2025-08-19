import tkinter as tk
from PIL import Image, ImageTk
import quizmodule
from pygame import mixer

class QuestionTemplate():
    def __init__(self, window, questionNumber:int,  questionTitle:str, questionOptions:list, correctOption):
        self.__questionTitle = questionTitle
        self.__questionOptions = questionOptions
        self.__tkinterWindow = window
        self.__questionNumber = questionNumber
        self.__correctOption = correctOption
    def createQuestionWindow(self, selection_made=None):
        for widget in self.__tkinterWindow.winfo_children():
            widget.destroy()
        popup = tk.Label(self.__tkinterWindow)
        popup.grid(sticky="s")
        def checkIfCorrect(optionButton):
            print(f"{optionButton.cget("text")}, {self.__correctOption}")
            if optionButton.cget("text") == self.__correctOption:
                is_correct = True
                popup.config(text="correct!!!", font=("Arial", 20), fg="#0FB800")
            else:
                is_correct = False
                popup.config(text=f"wrong!!! its {self.__correctOption}", font=("Arial", 20), fg="#B80000")
            
            #Disabling the button
            for option in tk_questionOptions:
                option.unbind("<Button-1>")  
                option.config(relief="sunken", bg="#CCCCCC", fg="#888888")
            if selection_made:
                selection_made(is_correct)

        tk_questionTitle = tk.Label(
            self.__tkinterWindow, 
            text=f"Question {self.__questionNumber}: {self.__questionTitle}", 
            font=("Arial", 36, "italic"), 
            justify="center",
            wraplength="750")
        tk_questionTitle.grid(row=2, column=0, columnspan=10, pady=(0, 20))
        tk_questionOptions = []
        buttonSFX = mixer.Sound("audio/button.mp3")
        for i in self.__questionOptions:
            button = tk.Button(self.__tkinterWindow, text=f"{i}", font=("Arial", 16))
            def onClick(event):
                buttonSFX.play()
                checkIfCorrect(event.widget)
            
            # Check answer on click
            button.bind("<Button-1>", onClick)
            tk_questionOptions.append(button)
        
        j = 0
        for i in tk_questionOptions:
            print(i)
            i.grid(columnspan=1,row=7,column=j, padx=10, pady=10)
            j+=1
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


