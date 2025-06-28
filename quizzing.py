import json
class Quiz():
    def __init__(self, jsfile):
        self.jsonf = jsfile

    def set_json(self):
        with open(self.jsonf, "r") as file:
            info = json.load(file)
    
    def set_title(self):
        with open(self.jsonf, "r") as file:
            info = json.load(file)
        self.title = info['title']
        print(self.title)


roygbiv = Quiz("quiz.json")
roygbiv.set_title()