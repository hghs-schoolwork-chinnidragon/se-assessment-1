import json
import random
from tkintermanipulation import config
import tkinter as tk
from PIL import Image, ImageTk


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
        self.__quizimage = Image.open(self.__questiondata['info'][1])
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
        qtext = tk.Label(window, text=f"""Welcome to the "{self.__title}" quiz! 
First, there are some things you need to know:""", font=("Arial", 60), wraplength=1420)
        qtext.pack()
        nextbutton = tk.Button(text="Next!", command=config(qtext, self.__quizinfo, "Arial", 60))


        # print(f'Welcome to the "{self.__title}" quiz!')
        # print("First, there are some things you need to know:")
        print(self.__quizinfo)
        input("Press enter to continue when you've finished reading!")
        score = 0
        #main loop of the function
        for q in range(0, len(self.__questions)):
            #so that it doesn't display "Question 0"
            print(f"Question {q+1}:")
            print(self.__questions[q])
            #printing the items of the list in a random order
            shuffled_copy = random.sample(self.__choices[q], len(self.__choices[q]))
            for item in shuffled_copy:
                print(f'* {item}')
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
        print(f"You got {score} out of {numq}! That's {(score/numq)*100}%!")
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





