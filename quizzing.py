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
            self.__questions = []
            self.__answers = []
            self.__potentans  = []
            for i in range(0, numq):
                self.__questions.append(self.__info['questions'][i])
                self.__answers.append(self.__info['questions'][i])
                self.__potentans.append(self.__info['questions'][i])
                # print(self.__questions, self.__answers, self.__potentans)
        load_title(self)
        load_qs(self)

        print(f'Welcome to the {self.__title} quiz!')
        question_number = 0
        score = 0
#         # needs to generate in random order + not show the same options (maybe just display all?)
#         for q in range(0, len(self.__questions)):
#             print(f"Question {question_number+1}:")
#             print(f"""{self.__questions[question_number]['question']}
# * {self.__potentans[question_number]['potential answer'][random.randint(0, 5)]}
# * {self.__potentans[question_number]['potential answer'][random.randint(0, 5)]}
# * {self.__potentans[question_number]['potential answer'][random.randint(0, 5)]}
# * {self.__answers[question_number]['correct answer']}""")
#             playerans = input("")
#             if playerans == {str(self.__answers[question_number]['correct answer'])}:
#                 score += 1
#                 print(score)
#             else:
#                 print(f"Sorry! The correct answer is {self.__answers[question_number]['correct answer']}")
#             question_number+= 1
#     #how can i return them as 2 seperate numbers not a tuple
#         return score, question_number
    
#     def score(scorenum, question_number):
#         print(f"You got {scorenum} out of {question_number} correct!")
        # print(f"That's {(scorenum/question_number)*100}%")

# need to make the Quiz as its own module and put these in a different file
roygbiv = Quiz("quiz.json")
# roygbiv.load_title()
# roygbiv.load_qs(2)
roygbiv.run_quiz()