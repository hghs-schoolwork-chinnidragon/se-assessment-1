import json
import tkinter as tk

root=tk.Tk()
def presentScoreHistory(jsfile, potentialQuizzes, root):

    data = []
    with open(jsfile, "r") as file:
        for record in file:
            try:
                data.append(json.loads(record))
            except json.decoder.JSONDecodeError:
                pass
    # print(data)
    scores = {}
    quiz_windows = {}
    for quiz in potentialQuizzes:
        quiz_windows[quiz] = tk.Toplevel(root)
        quiz_windows[quiz].title(f"{quiz} - Score History")
        quiz_windows[quiz].geometry("500x400")

        tk.Label(quiz_windows[quiz], text="Attempt", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=5)
        tk.Label(quiz_windows[quiz], text="Score", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=10, pady=5)
        tk.Label(quiz_windows[quiz], text="Percentage", font=("Arial", 12, "bold")).grid(row=0, column=2, padx=10, pady=5)

        scores[quiz] = {"score":None, "percentage":None}
        quiz_windows[quiz] = tk.Toplevel(root)
        heading = tk.Label(quiz_windows[quiz], text="your score")
        body = tk.Label(quiz_windows[quiz], text="", wraplength=500)
        heading2 = tk.Label(quiz_windows[quiz], text="ur percentage")
        body2 = tk.Label(quiz_windows[quiz], text="", wraplength=500)
        body2.grid(row=4)
        heading.grid(row=1)
        heading2.grid(row=3)
        body.grid(row=2)
        


    for record in data:
        quiznum = 0
        for quiz in potentialQuizzes:
            if record['quiz'] == potentialQuizzes[quiznum]:
                scores[quiz]["score"] = f"Your score: {record['score']}!"
                scores[quiz]["percentage"] = f"Your percentage: {round(record['percentage'])}%!"
                # .append([f"Your score: {record['score']}!", f"Your percentage: {round(record['percentage'])}!"])
                body.config(text=scores[quiz])
                body2.config(text=scores[quiz])
            quiznum+=1
    

    # window.mainloop()

    print(scores)


presentScoreHistory(
    "scorehistory.json", 
    [
        "What Colour is That?", 
        "Tiers of Colours!", 
        "Fun with Colour Relationships!", 
        "Understanding Hue, Saturation and Value"
    ],
    root
        )
root.mainloop()