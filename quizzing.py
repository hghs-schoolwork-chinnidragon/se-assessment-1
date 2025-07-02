import json
import random

def load_quinfo(filename):
    with open(filename, "r") as file:
        global info 
        info = json.load(file)

class Quiz():
    def __init__(self, jsfile):
        self.jsonf = jsfile
    
    def load_title(self):
        load_quinfo(self.jsonf)
        self.title = info['title']
        # print(self.title)

    def load_qs(self, numq):
        load_quinfo(self.jsonf)
        self.questions = []
        self.answers = []
        self.potentans  = []
        for i in range(1, numq+1):
            self.questions.append(info['questions'][f'Question {i}'][0])
            self.answers.append(info['questions'][f'Question {i}'][1])
            self.potentans.append(info['questions'][f'Question {i}'][2])

    def run_quiz(self):
        print(f'Welcome to the {self.title} quiz!')
        question_number = 0
        score = 0
        # needs to generate in random order + not show the same options (maybe just display all?)
        for q in range(0, len(self.questions)):
            print(f"Question {question_number+1}:")
            print(f"""{self.questions[question_number]['question']}
* {self.potentans[question_number]['potential answer'][random.randint(0, 5)]}
* {self.potentans[question_number]['potential answer'][random.randint(0, 5)]}
* {self.potentans[question_number]['potential answer'][random.randint(0, 5)]}
* {self.answers[question_number]['correct answer']}""")
            playerans = input("")
            if playerans == {str(self.answers[question_number]['correct answer'])}:
                score += 1
                print(score)
            else:
                print(f"Sorry! The correct answer is {self.answers[question_number]['correct answer']}")
            question_number+= 1
    #how can i return them as 2 seperate numbers not a tuple
        return score, question_number
    
    def score(scorenum, question_number):
        print(f"You got {scorenum} out of {question_number} correct!")
        # print(f"That's {(scorenum/question_number)*100}%")

# need to make the Quiz as its own module and put these in a different file
roygbiv = Quiz("quiz.json")
roygbiv.load_title()
roygbiv.load_qs(2)
roygbiv.score(roygbiv.run_quiz())