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
        qnum = 0
        for q in self.questions:
            print(q['question'])
            print(q['correct answer'])
            for ans in q['potential answer']:
                print(ans)


        # print(self.questions)
        



roygbiv = Quiz("quiz.json")
roygbiv.load_title()
roygbiv.load_qs()