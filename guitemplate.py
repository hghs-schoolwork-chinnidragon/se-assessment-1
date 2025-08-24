import tkinter as tk
from PIL import Image, ImageTk
import quizmodule
from pygame import mixer

class QuestionTemplate():
    def __init__(self, window, questionNumber:int,  questionTitle:str, questionOptions:list, correctOption, canvas):
        self.__questionTitle = questionTitle
        self.__questionOptions = questionOptions
        self.__tkinterWindow = window
        self.__questionNumber = questionNumber
        self.__correctOption = correctOption
        self.__buttons = []
        self.__canvas = canvas

    def createQuestionWindow(self, selection_made=None):
        # Clear canvas
        self.__canvas.delete("all")
        self.__buttons = []  # Clear button references

        self.__canvas.create_text(400, 35, text=f"Question {self.__questionNumber}", font=("Noteworthy", 24, "bold"), fill="#081480")


        popup = tk.Label(self.__tkinterWindow)
        # self.__canvas.create_window(400, 500, window=popup)

        def checkIfCorrect(optionButton):
            if optionButton.cget("text") == self.__correctOption:
                is_correct = True
                popup.config(text="Correct!!!", font=("Arial", 20), fg="#0FB800")
                self.__canvas.create_window(400, 400, window=popup)
            else:
                is_correct = False
                popup.config(text=f"Wrong!!! It's {self.__correctOption}", font=("Arial", 20), fg="#B80000")
                self.__canvas.create_window(400, 400, window=popup)
            
            #Disabling the button
            for option in self.__buttons:
                option.unbind("<Button-1>")  
                option.config(relief="sunken", bg="#CCCCCC", fg="#888888")
            if selection_made:
                selection_made(is_correct)

# Question title
        self.__canvas.create_text(
            400, 100, 
            text=f"{self.__questionTitle}", 
            font=("Chalkboard", 24, "italic"), 
            fill="#80080C",
            justify="center",
            width=750
        )

        buttonSFX = mixer.Sound("audio/button.mp3")
        button_y = 200
        for i in self.__questionOptions:
            button = tk.Button(self.__tkinterWindow, text=f"{i}", font=("Arial", 16), width=40)
            def onClick(event):
                buttonSFX.play()
                checkIfCorrect(event.widget)
            
            # Check answer on click
            button.bind("<Button-1>", onClick)

            #Add button to canvas
            self.__canvas.create_window(400, button_y, window=button)
            button_y += 60

            #Store reference
            self.__buttons.append(button)
    def configInfo(self, quizImage, quizInfo, PIL, button, buttoncommand):
        # Clear canvas
        self.__canvas.delete("all")
        self.__canvas.create_text(400, 35, text="Quiz Information", font=("Arial", 24, "bold"), fill="white")

        #Load and display image
        if not PIL == None:
            labelImage = ImageTk.PhotoImage(quizImage)
        else:
            labelImage = tk.PhotoImage(file=quizImage)
        #Store reference
        self.__canvas.image=labelImage
        # Draw image on canvas
        self.__canvas.create_image(600, 200, image=labelImage)

        # Display quiz info text
        self.__canvas.create_text(
            250, 200,
            text=quizInfo,
            font=("Arial", 16),
            width=400,
            justify="left"
        )

        button.config(command=buttoncommand)
        self.__canvas.create_window(400, 400, window=button)