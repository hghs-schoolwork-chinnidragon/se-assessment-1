import json
import random
import tkinter as tk
from PIL import Image, ImageTk
import guitemplate



class Quiz:
    #retrieving data from provided file
    def __init__(self, jsfile):
        self.__jsfile = jsfile
        with open(self.__jsfile, "r") as file:
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
        self.__images = []
    @staticmethod
    def resizeImg(newWidth, image):
        #newwidth divided by width/height OR newwidth * height/width
        #resizing the image while keeping the aspect ratio
        try:
            pilImage = Image.open(image).convert("RGBA")
        except AttributeError: #already a PIL image
            pilImage = image
        print (f"{pilImage.width}/{pilImage.height}")
        # ratio = pilImage.width/pilImage.height
        orig_width, orig_height = pilImage.size
        ratio = orig_width / orig_height
        newHeight = round(newWidth/ratio)
        resizedImage = pilImage.resize([newWidth, newHeight])
        # print(f"resized! dimensions {resizedImage.width}x{resizedImage.height}")
        return(resizedImage)
    def run(self):
        window = tk.Toplevel()
        # window.geometry("1440x1024")
        window.title(f"{self.__title}")
        # while True:
        print(self.__quizimage)
        quizImage = Image.open(self.__questiondata['info'][2])
        resizedQuizImage = self.resizeImg(200, quizImage)
        self.__images.append(resizedQuizImage)
        qtext = tk.Label(
            window, 
            text=f"""Welcome to the "{self.__title}" quiz! 
First, there are some things you need to know:""",
            font=("Arial", 48), 
            wraplength=500
            )
        # qtext.grid(row=5, column=5,  columnspan=10, rowspan=10)
        qtext.grid()
        def config_info():
            qt = guitemplate.QuestionTemplate(
                window,
                None,
                None, 
                None,
                None)
            qt.configInfo(
                resizedQuizImage,
                self.__quizinfo, 
                qtext, 
                True, 
                nextbutton, 
                run_questions)
        def run_questions():
            for q in range(0, len(self.__questions)):
                shuffled_copy = random.sample(self.__choices[q], len(self.__choices[q]))
                config = guitemplate.QuestionTemplate(window, q+1, self.__questions[q], shuffled_copy, self.__answers[q])
                config.createQuestionWindow()
            #     for item in shuffled_copy:
            #         print(f'* {item}')
                # config = guitemplate.QuestionTemplate(window, self.__questions[q], shuffled_copy)
            
            
            # qtext.image = resizedQuizImage
        
        # def clear_screen(window):
        #     for widget in window.winfo_children():
        #         widget.destroy()  
        
        nextbutton = tk.Button(window, text="Next!", command=config_info)
        nextbutton.grid(column=5)
        # window.mainloop()

        # config_questions = config.createQuestionWindow()
    #         if qtext.cget("text") == f"""Welcome to the "{self.__title}" quiz! 
    # First, there are some things you need to know:""":
    #             nextbutton = tk.Button(text="Next!", command=config_info)
    #         else:
    #             nextbutton = tk.Button(text="Let's go!", command=clear_screen)
    #             break
    #         nextbutton.grid()

        # score = 0
        # #main loop of the function
        # for q in range(0, len(self.__questions)):
        #     shuffled_copy = random.sample(self.__choices[q], len(self.__choices[q]))
        #     config = guitemplate.QuestionTemplate(window, q+1, self.__questions[q], shuffled_copy, self.__answers[q])
        #     config.createQuestionWindow()
        #     # print(f"Question {q+1}:")
        #     # print(self.__questions[q])
        #     #printing the items of the list in a random order
        #     # shuffled_copy = random.sample(self.__choices[q], len(self.__choices[q]))
        #     for item in shuffled_copy:
        #         print(f'* {item}')
        #     # config = guitemplate.QuestionTemplate(window, self.__questions[q], shuffled_copy)
        #     config.createQuestionWindow()
            

            #will change to tkinter
            # player_choice = input("-> ")
            # if player_choice.lower() == self.__answers[q].lower():
            #     print("CORRECTTT")
            #     score +=1
            # else:
            #     print(f"INCORRECT its {self.__answers[q]}!")
    # #DEBUG
    #     score = 7
        # numq = len(self.__questiondata['questions'])
        # print(f"You got {score} out of {numq}! That's {round((score/numq)*100)}%!")
        # data = {
        #         "quiz": self.__title,
        #         "score": score,
        #         "percentage": score/numq*100
        #         }
        
        # with open('scorehistory.json', 'a') as file:
        #     json.dump(data, file)
        window.mainloop()

    def getTitle(self):
        return(self.__title)
    
    def getImage(self):
        return(self.__quizimage)
    
    def getFile(self):
        return(self.__jsfile)






