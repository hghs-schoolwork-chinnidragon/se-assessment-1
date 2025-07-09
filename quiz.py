import json
import random


class Quiz:
    #retrieving data from provided file
    def __init__(self, jsfile):
        with open(jsfile, "r") as file:
            self.__questiondata = json.load(file)
        #retrieving data
        self.__title = self.__questiondata['title']
        numq = len(self.__questiondata['questions'])
        #retrieving the questions, answers and choices -- MUST be 'question', 'correctAnswer' and 'choices'
        self.__questions = []
        self.__answers = []
        self.__choices  = []
        for i in range(0, numq):
            self.__questions.append(self.__questiondata['questions'][i]['question'])
            self.__answers.append(self.__questiondata['questions'][i]['correctAnswer'])
            self.__choices.append(self.__questiondata['questions'][i]['choices'])

    def run_quiz(self):
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
        numq = len(self.__questiondata['questions'])
        print(f"You got {score} out of {numq}! That's {(score/numq)*100}%!")


if __name__ == "__main__":
    Quiz("roygbiv.json")


