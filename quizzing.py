import json
import random


class Quiz:
    #retrieving data from provided file
    def __init__(self, jsfile):
        self.__jsonf = jsfile
        with open(self.__jsonf, "r") as file:
            self.__info = json.load(file)
        # print(self.__info)

    def run_quiz(self):
        def load_title(self):
            self.__title = self.__info['title']
        def load_qs(self):
            #retrieving number of questions
            numq = len(self.__info['questions'])
            #retrieving the questions, answers and choices -- MUST be 'question', 'correctAnswer' and 'choices'
            self.__questions = []
            self.__answers = []
            self.__choices  = []
            for i in range(0, numq):
                self.__questions.append(self.__info['questions'][i]['question'])
                self.__answers.append(self.__info['questions'][i]['correctAnswer'])
                self.__choices.append(self.__info['questions'][i]['choices'])
                # print(self.__choices)
        #loading the title and the questions
        load_title(self)
        load_qs(self)
        print(f'Welcome to the "{self.__title}" quiz!')
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
            if player_choice == self.__answers[q]:
                print("CORRECTTT")
                score +=1
            else:
                print("INCORRECT")

roygbiv = Quiz("quiz.json")
# roygbiv.load_title()
# roygbiv.load_qs(2)
roygbiv.run_quiz()