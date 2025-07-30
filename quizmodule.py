import json
import random
import tkinter as tk
from PIL import Image, ImageTk
import guitemplate


class Quiz:
    #retrieving data from provided file
    def __init__(self, jsfile):
        with open(jsfile, "r") as file:
            self.__questiondata = json.load(file)
        #retrieving data
        self.__title = self.__questiondata['title']
        #read the info from the text file that the key directs it to
        self.__quizinfo = self.__questiondata['info'][0]
        with open(self.__quizinfo, "r") as file:
            self.__quizinfo = file.read()
        numq = len(self.__questiondata['questions'])
        #retrieve the image associated with the info
        self.__quizimage = self.__questiondata['info'][1]
        #retrieving the questions, answers and choices -- MUST be 'question', 'correctAnswer' and 'choices'
        self.__questions = []
        self.__answers = []
        self.__choices  = []
        for i in range(0, numq):
            self.__questions.append(self.__questiondata['questions'][i]['question'])
            self.__answers.append(self.__questiondata['questions'][i]['correctAnswer'])
            self.__choices.append(self.__questiondata['questions'][i]['choices'])

    def run(self):
        window = tk.Tk()
        window.geometry("1440x1024")
        while True:
            qtext = tk.Label(window, text=f"""Welcome to the "{self.__title}" quiz! 
    First, there are some things you need to know:""", font=("Arial", 60), wraplength=1420)
            qtext.grid(
                row=3
            )

            config_info = guitemplate.QuestionTemplate.configInfo(self.__quizimage, self.__quizinfo, qtext)
            def clear_screen(window):
                for widget in window.winfo_children():
                    widget.destroy()       # config = guitemplate.QuestionTemplate(window, self.__questions[q], shuffled_copy)
            # config_questions = config.createQuestionWindow()
            if qtext.cget("text") == f"""Welcome to the "{self.__title}" quiz! 
    First, there are some things you need to know:""":
                nextbutton = tk.Button(text="Next!", command=config_info)
            else:
                nextbutton = tk.Button(text="Let's go!", command=clear_screen)
                break
            nextbutton.grid()

        score = 0
        #main loop of the function
        for q in range(0, len(self.__questions)):
            config = guitemplate.QuestionTemplate(window, )
            config.createQuestionWindow()
            print(f"Question {q+1}:")
            print(self.__questions[q])
            #printing the items of the list in a random order
            shuffled_copy = random.sample(self.__choices[q], len(self.__choices[q]))
            for item in shuffled_copy:
                print(f'* {item}')
            config = guitemplate.QuestionTemplate(window, self.__questions[q], shuffled_copy)
            config_questions = config.createQuestionWindow()
            

            #will change to tkinter
            player_choice = input("-> ")
            if player_choice.lower() == self.__answers[q].lower():
                print("CORRECTTT")
                score +=1
            else:
                print(f"INCORRECT its {self.__answers[q]}!")
    # #DEBUG
    #     score = 7
        numq = len(self.__questiondata['questions'])
        print(f"You got {score} out of {numq}! That's {round((score/numq)*100)}%!")
        data = {
                "quiz": self.__title,
                "score": score,
                "percentage": score/numq*100
                }
        
        with open('scorehistory.json', 'a') as file:
            json.dump(data, file)
        window.mainloop()

    def getTitle(self):
        return(self.__title)
    
    def getImage(self):
        return(self.__quizimage)





