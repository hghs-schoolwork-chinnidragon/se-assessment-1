import json

def load_quinfo(filename):
    with open(filename, "r") as file:
        global info 
        info = json.load(file)

class Quiz():
    def __init__(self, jsfile):
        self.jsonf = jsfile

    # def set_json(self):
    #     with open(self.jsonf, "r") as file:
    #         info = json.load(file)
    
    def load_title(self):
        load_quinfo(self.jsonf)
        self.title = info['title']
        # print(self.title)

    def load_qs(self):
        load_quinfo(self.jsonf)
        self.questions = info['questions']
        print(self.questions)
        # qnum = 0
        # print(info['questions'])
        # for q in self.questions:
        #     print(q)
        #     print(q['question'])
        #     print(q['correct answer'])
        #     for ans in q['potential answer']:
        #         print(ans)

#i'm trying to get the questiosn AND answers loaded but idk how to :(

        print(self.questions)
    def run_quiz(self):
        print(f'Welcome to the {self.title} quiz!')
        qnum = 0
        score = 0
        #for q in questions (when this works)
            #print (f"Question {qnum}":)
            #print (f"{question name}")
            #print correct answer + random potential answers

            #ans = user inputted answer
            #if ans == correct answer:
                #score +=1
            #else:
                #print "too bad" or smth
            #qnum +=1



roygbiv = Quiz("quiz.json")
roygbiv.load_title()
roygbiv.load_qs()