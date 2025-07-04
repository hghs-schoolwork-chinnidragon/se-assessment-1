import json
import random


class Quiz:
    def __init__(self, jsfile):
        self.__jsonf = jsfile
        with open(jsfile, "r") as file:
            self.__info = json.load(file)
        print(self.__info)
    def load_title(self):
        self.__title = self.__info['title']
        # print(self.title)

    def load_qs(self):
        self.__questions = []
        self.__answers = []
        self.__potentans  = []
        for i in range(1, numq+1):
            self.__questions.append(info['questions'][f'Question {i}'][0])
            self.__answers.append(info['questions'][f'Question {i}'][1])
            self.__potentans.append(info['questions'][f'Question {i}'][2])

    def run_quiz(self):
        print(f'Welcome to the {self.__title} quiz!')
        question_number = 0
        score = 0
        # needs to generate in random order + not show the same options (maybe just display all?)
        for q in range(0, len(self.__questions)):
            print(f"Question {question_number+1}:")
            print(f"""{self.__questions[question_number]['question']}
* {self.__potentans[question_number]['potential answer'][random.randint(0, 5)]}
* {self.__potentans[question_number]['potential answer'][random.randint(0, 5)]}
* {self.__potentans[question_number]['potential answer'][random.randint(0, 5)]}
* {self.__answers[question_number]['correct answer']}""")
            playerans = input("")
            if playerans == {str(self.__answers[question_number]['correct answer'])}:
                score += 1
                print(score)
            else:
                print(f"Sorry! The correct answer is {self.__answers[question_number]['correct answer']}")
            question_number+= 1
    #how can i return them as 2 seperate numbers not a tuple
        return score, question_number
    
    def score(scorenum, question_number):
        print(f"You got {scorenum} out of {question_number} correct!")
        # print(f"That's {(scorenum/question_number)*100}%")

# need to make the Quiz as its own module and put these in a different file
roygbiv = Quiz("quiz.json")
# roygbiv.load_title()
# roygbiv.load_qs(2)
# roygbiv.score(roygbiv.run_quiz())