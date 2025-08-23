import json
import random
import tkinter as tk
from PIL import Image, ImageTk
import guitemplate
from pygame import mixer



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
        mixer.music.load("audio/Kick Shock.mp3")
        mixer.music.play(-1,0.0)
        window = tk.Toplevel()
        window.geometry("+50+50")
        window.title(f"{self.__title}")
        self.current_question = 0
        self.score = 0
        # while True:
        self.nextbutton = tk.Button(window, text="Next!")
        self.nextbutton.grid(column=5)

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
                self.nextbutton, 
                show_next_question)

            #     for item in shuffled_copy:
        def show_next_question():
            # Clear previous question widgets if any
            for widget in window.winfo_children():
                if widget != self.nextbutton:  # Keep the next button
                    widget.destroy()
            
            # If all questions answered, show results
            if self.current_question >= len(self.__questions):
                show_results()
                return
            
            # Show current question
            q = self.current_question
            shuffled_copy = random.sample(self.__choices[q], len(self.__choices[q]))
            
            # Create question template with answer callback
            self.config = guitemplate.QuestionTemplate(
                window,
                q+1, 
                self.__questions[q], 
                shuffled_copy, 
                self.__answers[q]
            )
            
            # Pass callback function to handle when answer is selected
            self.config.createQuestionWindow(on_answer_selected)
            
            # Hide next button until answer is selected
            self.nextbutton.grid_remove()
            
        self.nextbutton.config(command=config_info)
        
        def on_answer_selected(is_correct):
            self.current_question += 1
            if is_correct:
                self.score += 1
            
            self.nextbutton = tk.Button(window, text="Next Question", command=show_next_question)
            self.nextbutton.grid()
            
        # Show final results
        def show_results():
            for widget in window.winfo_children():
                widget.destroy()
            
            result_text = f"""Quiz Complete!\nYou got {self.score} out of {len(self.__questions)}.
\nThat's {round((self.score/len(self.__questions))*100)}%!"""
            
            result_label = tk.Label(
                window,
                text=result_text,
                font=("Arial", 24),
                wraplength=500
            )
            result_label.pack(pady=50)
            
            # Save score data
            data = {
                "quiz": self.__title,
                "score": self.score,
                "percentage": (self.score/len(self.__questions))*100
            }
            
            with open('scorehistory.json', 'a') as file:
                json.dump(data, file)
                print("", file=file)
            
            if (self.score/len(self.__questions))*100 > 80:
                data = "pass"
            else:
                data="fail"
            with open(f'{self.__title}.txt', 'a') as file:
                json.dump(data, file)
                print("", file=file)

            def close():
                mixer.music.load("audio/Pookatori and Friends.mp3")
                mixer.music.play(-1,0.0)
                window.destroy()

            close_button = tk.Button(window, text="Close", command=close)
            close_button.pack(pady=20)
        
            
        # Keeping track of images to prevent garbage collection
        window.images = self.__images
        window.mainloop()

    def getTitle(self):
        return(self.__title)
    
    def getImage(self):
        return(self.__quizimage)
    
    def getFile(self):
        return(self.__jsfile)






