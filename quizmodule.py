import json
import random
import tkinter as tk
from PIL import Image, ImageTk
import guitemplate
from pygame import mixer



class Quiz:
    #Retrieve data from provided file
    def __init__(self, jsfile):
        self.__jsfile = jsfile
        with open(self.__jsfile, "r") as file:
            self.__questiondata = json.load(file)
        #Retrieve data
        self.__title = self.__questiondata['title']
        #Read the info from the text file that the key directs it to
        self.__quizinfo = self.__questiondata['info'][0]
        with open(self.__quizinfo, "r") as file:
            self.__quizinfo = file.read()
        numq = len(self.__questiondata['questions'])
        #Retrieve the image associated with the info
        self.__quizimage = self.__questiondata['info'][1]
        
        #Retrieving the questions, answers and choices -- MUST be 'question', 'correctAnswer' and 'choices'
        self.__questions = []
        self.__answers = []
        self.__choices  = []
        for i in range(0, numq):
            self.__questions.append(self.__questiondata['questions'][i]['question'])
            self.__answers.append(self.__questiondata['questions'][i]['correctAnswer'])
            self.__choices.append(self.__questiondata['questions'][i]['choices'])
        #Img referencing for garbage collection
        self.__images = []
    @staticmethod
    def resizeImg(newWidth, image):
        #Resizing the image while keeping the aspect ratio
        try:
            pilImage = Image.open(image).convert("RGBA")
        except AttributeError: #already a PIL image
            pilImage = image
        orig_width, orig_height = pilImage.size
        ratio = orig_width / orig_height
        newHeight = round(newWidth/ratio)
        resizedImage = pilImage.resize([newWidth, newHeight])
        return(resizedImage)

    def run(self):
        #New music
        mixer.music.load("audio/Kick Shock.mp3")
        mixer.music.play(-1,0.0)
        #Creating window
        window = tk.Toplevel()
        window.geometry("800x600+50+50")
        #Making window title the quiz name
        window.title(f"{self.__title}")

        #Creating main canvas
        main_canvas = tk.Canvas(window, width=800, height=800, bg="#f0f0ff", highlightthickness=0)
        main_canvas.pack(fill="both", expand=True)

        #Initialising variables
        self.current_question = 0
        self.score = 0
        self.window = window
        self.main_canvas = main_canvas
        self.buttons = []
        
        self.nextbutton = tk.Button(window, text="Next!", font="Chalkboard")
        main_canvas.create_window(700, 550, window=self.nextbutton)

        # Loading and displaying quiz image
        quizImage = Image.open(self.__questiondata['info'][2])
        resizedQuizImage = self.resizeImg(200, quizImage)
        quiz_photo = ImageTk.PhotoImage(resizedQuizImage)
        self.__images.append(quiz_photo)
        
        # Display image on canvas
        main_canvas.create_image(400, 450, image=quiz_photo)

        main_canvas.create_text(
            400, 200,  # x and y coordinates (center of canvas)
            text=f"""Welcome to the "{self.__title}" quiz! 
First, there are some things you need to know:""",
            font=("Arial", 24, "bold"), 
            fill="#800808",
            width=600,
            justify="center"
        )


        def config_info():
            main_canvas.delete("all")
            main_canvas.create_image(600, 150, image=quiz_photo)
            main_canvas.create_text(
                400, 300,
                text=self.__quizinfo,
                font=("Chalkboard", 12),
                fill="#000000",
                width=600,
                justify="left"
            )
            self.nextbutton.config(text="Start Quiz", command=show_next_question)
            main_canvas.create_window(400, 500, window=self.nextbutton)

        def show_next_question():
            main_canvas.delete("all")

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
                self.__answers[q],
                main_canvas
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
            
            self.nextbutton.config(text="Next Question", command=show_next_question)
            main_canvas.create_window(400, 135, window=self.nextbutton)
            
        # Show final results
        def show_results():
            for widget in window.winfo_children():
                widget.destroy()
            main_canvas = tk.Canvas(window, width=800, height=800, bg="#f0f0ff", highlightthickness=0)
            main_canvas.pack(fill="both", expand=True)
            result_text = f"""Quiz Complete!\nYou got {self.score} out of {len(self.__questions)}.
\nThat's {round((self.score/len(self.__questions))*100)}%!"""
            
            result_label = tk.Label(
                window,
                text=result_text,
                font=("Chalkboard", 24),
                fg="#AA1CA8",
                wraplength=500
            )
            main_canvas.create_window(150, 300, window=result_label)
            
            # Save score data
            data = {
                "quiz": self.__title,
                "score": self.score,
                "percentage": (self.score/len(self.__questions))*100
            }
            
            with open('scorehistory.json', 'a') as file:
                json.dump(data, file)

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






