import quiz
import tkinter as tk
class Menu:
    @staticmethod
    def createwindow():
        window = tk.Tk()

    def init(self, quizzes):
        print(quizzes[0].getTitle(), quizzes[0].getImage())
q_whatColourIsThat = quiz.Quiz("whatColourIsThat.json")
q_allAboutHSV = quiz.Quiz("allAboutHSV.json")
# q_whatColourIsThat.run()
q_allAboutHSV.run()