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

    scores = {}
    quiz_windows = {}
    for quiz in potentialQuizzes:
        quiz_windows[quiz] = tk.Toplevel(root)
        quiz_windows[quiz].title(f"{quiz} - Score History")
        quiz_windows[quiz].geometry("500x400")

        tk.Label(quiz_windows[quiz], text="Score", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=5)
        tk.Label(quiz_windows[quiz], text="Percentage", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=10, pady=5)



    for record in data:
        quiznum = 0
        for quiz in potentialQuizzes:
            if record['quiz'] == potentialQuizzes[quiznum]:
                scores[quiz]["score"] = f"Your score: {record['score']}!"
                scores[quiz]["percentage"] = f"Your percentage: {round(record['percentage'])}%!"
                # .append([f"Your score: {record['score']}!", f"Your percentage: {round(record['percentage'])}!"])
                score = tk.Label(quiz_windows[quiz], text=scores[quiz]["score"])
                score.grid(column=0)
                percent = tk.Label(quiz_windows[quiz], text=scores[quiz]["percentage"])
                percent.grid(column=1)
            quiznum+=1
    

    # window.mainloop()



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