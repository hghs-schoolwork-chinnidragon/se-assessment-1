import json
import random
import tkinter as tk
from PIL import Image, ImageTk
import guitemplate
from pygame import mixer


class Quiz:
    # Quiz class that handles loading, displaying and running quizzes from JSON files
    # Manages the quiz interface, question flow, and scoring.

    def __init__(self, jsfile):
        """
        Initialize the quiz by loading data from a JSON file
        
        Parameters:
            jsfile (str): Path to the JSON file containing quiz data
        """
        self.__jsfile = jsfile
        # Load quiz data from JSON file
        with open(self.__jsfile, "r") as file:
            self.__questiondata = json.load(file)
            
        # Extract quiz title from JSON
        self.__title = self.__questiondata['title']
        
        # Load quiz info text from the file specified in JSON
        self.__quizinfo = self.__questiondata['info'][0]
        with open(self.__quizinfo, "r") as file:
            self.__quizinfo = file.read()
            
        # Count how many questions are in the quiz
        numq = len(self.__questiondata['questions'])
        
        # Get the path to quiz image
        self.__quizimage = self.__questiondata['info'][1]
        
        # Extract questions, answers and choices from JSON
        # JSON must contain 'question', 'correctAnswer', and 'choices' keys
        self.__questions = []  # List to store question texts
        self.__answers = []    # List to store correct answers
        self.__choices = []    # List to store all answer choices
        
        # Process each question in the JSON
        for i in range(0, numq):
            self.__questions.append(self.__questiondata['questions'][i]['question'])
            self.__answers.append(self.__questiondata['questions'][i]['correctAnswer'])
            self.__choices.append(self.__questiondata['questions'][i]['choices'])
            
        # List to store image references (prevents garbage collection)
        self.__images = []
        with open("scorehistory.json", "r") as file:
            completed = False
            for line in file:
                try:
                    record = json.loads(line)
                    if record.get("quiz") == self.__title:
                        completed = True
                        break
                except json.JSONDecodeError:
                    continue
        if completed:
            self.__completed = True
        else:
            self.__completed = False


        
    @staticmethod
    def resizeImg(newWidth, image):
        # Resize an image while maintaining its aspect ratio
        
        # Parameters:
        #     newWidth (int): Desired width of the resized image
        #     image (str or PIL.Image): Path to image or PIL Image object
            
        # Returns:
        #     PIL.Image: Resized image

        # Check if input is file path or PIL Image
        try:
            pilImage = Image.open(image).convert("RGBA")
        except AttributeError:  # Already a PIL image
            pilImage = image
            
        # Calculate new height based on original aspect ratio
        orig_width, orig_height = pilImage.size
        ratio = orig_width / orig_height
        newHeight = round(newWidth/ratio)
        
        # Resize image and return
        resizedImage = pilImage.resize([newWidth, newHeight])
        return(resizedImage)

    def run(self):
        """
        Run the quiz - creates and manages the main quiz interface
        Displays welcome screen, questions, and results
        """
        # Change background music for quiz
        mixer.music.load("audio/Kick Shock.mp3")
        mixer.music.play(-1, 0.0)  # Play indefinitely (-1) from start (0.0)
        
        # Create main quiz window
        window = tk.Toplevel()
        window.geometry("800x600+50+50")
        window.title(f"{self.__title}")

        # Create main canvas for drawing quiz elements
        main_canvas = tk.Canvas(window, width=800, height=800, bg="#f0f0ff", highlightthickness=0)
        main_canvas.pack(fill="both", expand=True)

        # Initialize quiz state variables
        self.current_question = 0  # Tracks current question index
        self.score = 0  # Tracks user's score
        self.window = window  # Store window reference
        self.main_canvas = main_canvas  # Store canvas reference
        self.buttons = []  # List to track buttons
        
        # Create Next button and add to canvas
        self.nextbutton = tk.Button(window, text="Next!", font="Chalkboard")
        main_canvas.create_window(700, 550, window=self.nextbutton)

        # Load and prepare quiz image
        quizImage = Image.open(self.__questiondata['info'][2])
        resizedQuizImage = self.resizeImg(200, quizImage)
        quiz_photo = ImageTk.PhotoImage(resizedQuizImage)
        self.__images.append(quiz_photo)  # Store reference to prevent garbage collection
        
        # Display quiz image on welcome screen
        main_canvas.create_image(400, 450, image=quiz_photo)

        if not self.__completed:
        # Display welcome message
            main_canvas.create_text(
                400, 200,  # Center horizontally, position vertically
                text=f"""Welcome to the "{self.__title}" quiz! 
    First, there are some things you need to know:""",
                font=("Arial", 24, "bold"), 
                fill="#800808",  # Dark red color
                width=600,  # Text wrapping width
                justify="center"
            )
        else:
            main_canvas.create_text(
                400, 200,  # Center horizontally, position vertically
                text=f"""You've already done the "{self.__title}" quiz, but you can still do it again! 
    Here are some things you probably know:""",
                font=("Arial", 24, "bold"), 
                fill="#800808",  # Dark red color
                width=600,  # Text wrapping width
                justify="center"
            )

        def config_info():
            """
            Shows the quiz info screen with detailed instructions
            Triggered when user clicks Next from welcome screen
            """
            # Clear canvas content
            main_canvas.delete("all")
            
            # Show quiz image
            quiz_photo = ImageTk.PhotoImage(self.resizeImg(50, quizImage))
            main_canvas.create_image(600, 150, image=quiz_photo)
            
            # Show quiz information text
            main_canvas.create_text(
                400, 300,
                text=self.__quizinfo,
                font=("Chalkboard", 12),
                fill="#000000",
                width=600,
                justify="left"
            )
            
            # Change Next button to Start Quiz and update its action
            self.nextbutton.config(text="Start Quiz", command=show_next_question)
            main_canvas.create_window(400, 500, window=self.nextbutton)

        def show_next_question():
            """
            Displays the next question in the quiz
            If no more questions, shows results
            """
            # Clear canvas
            main_canvas.delete("all")

            # Check if all questions have been answered
            if self.current_question >= len(self.__questions):
                show_results()  # Show final results
                return
            
            # Get current question index
            q = self.current_question
            
            # Shuffle answer choices for randomization
            shuffled_copy = random.sample(self.__choices[q], len(self.__choices[q]))
            
            # Create question template with current question data
            self.config = guitemplate.QuestionTemplate(
                window,  # Parent window
                q+1,     # Question number (1-based for display)
                self.__questions[q],  # Question text
                shuffled_copy,        # Randomized choices
                self.__answers[q],    # Correct answer
                main_canvas           # Canvas to draw on
            )
            
            # Create the question UI and set callback for when user answers
            self.config.createQuestionWindow(on_answer_selected)
            
            # Hide next button until answer is selected
            self.nextbutton.grid_remove()
            
        # Set the initial Next button to show quiz info
        self.nextbutton.config(command=config_info)
        
        def on_answer_selected(is_correct):
            """
            Callback when user selects an answer
            Updates score and prepares for next question
            
            Parameters:
                is_correct (bool): Whether the selected answer was correct
            """
            # Move to next question
            self.current_question += 1
            
            # Update score if answer was correct
            if is_correct:
                self.score += 1
            
            # Configure next button for next question
            self.nextbutton.config(text="Next Question", command=show_next_question)
            
            # Show next button on canvas
            main_canvas.create_window(600, 35, window=self.nextbutton)
            
        def show_results():
            """
            Display final quiz results and score
            """
            # Remove all widgets
            for widget in window.winfo_children():
                widget.destroy()
                
            # Create new canvas for results
            main_canvas = tk.Canvas(window, bg="#f0f0ff", highlightthickness=0)
            main_canvas.pack(fill="both", expand=True)
            
            # Format results text with score and percentage
            result_text = f"""Quiz Complete!\nYou got {self.score} out of {len(self.__questions)}.
\nThat's {round((self.score/len(self.__questions))*100)}%!"""
            
            main_canvas.create_text(150, 300, text=result_text, font=("Chalkboard", 24), fill="#AA1CA8",  width=500)
            
            # Save score data to JSON file
            data = {
                "quiz": self.__title,
                "score": self.score,
                "percentage": (self.score/len(self.__questions))*100
            }
            
            # Append to score history file
            with open('scorehistory.json', 'a') as file:
                json.dump(data, file)

            def close():
                # Close quiz and return to menu music
                # Change music back to menu music
                mixer.music.load("audio/Pookatori and Friends.mp3")
                mixer.music.play(-1, 0.0)
                # Close quiz window
                window.destroy()

            # Create close button
            close_button = tk.Button(window, text="Close", command=close)
            main_canvas.create_window(150, 400, window=close_button)
        
        # Store image references to prevent garbage collection
        window.images = self.__images
        
        # Start the quiz window event loop
        window.mainloop()

    def getTitle(self):
        # Return the quiz title
        return(self.__title)
    
    def getImage(self):
        # Return the path to the quiz image
        return(self.__quizimage)
    
    def getFile(self):
        # Return the path to the quiz JSON file
        return(self.__jsfile)