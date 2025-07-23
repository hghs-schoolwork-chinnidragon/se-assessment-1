from quiz import Quiz
import tkinter as tk
class Menu:
    # @staticmethod
    # def createwindow():
    #     window = tk.Tk()

    def __init__(self, quizzes):
        window = tk.Tk()
        quizWidgets = []
        for i in range(0, len(quizzes)):
            print(quizzes[i].getTitle(), quizzes[i].getImage())
            quizWidget = tk.Label(window, text=f"{Quiz.getTitle()}", image=f"{Quiz.getImage}")
            quizWidgets.append(quizWidget)

        for i in range(0, len(quizWidgets)):
            quizWidgets[i].pack(window)
    
q_whatColourIsThat = Quiz("whatColourIsThat.json")
q_allAboutHSV = Quiz("allAboutHSV.json")
# q_whatColourIsThat.run()
# q_allAboutHSV.run()

menu = Menu([q_allAboutHSV, q_whatColourIsThat])
