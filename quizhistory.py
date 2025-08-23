import json

def presentScoreHistory(jsfile, potentialQuizzes):
    data = []
    with open(jsfile, "r") as file:
        for line in file:
            try:
                data.append(json.loads(line))
            except json.decoder.JSONDecodeError:
                pass
    # print(data)
    scores = {}
    for quiz in potentialQuizzes:
        scores[quiz] = []


    for line in data:
        quiznum = 0
        for quiz in potentialQuizzes:
            # print (line["quiz"])
            # print(potentialQuizzes[quiznum])
            if line['quiz'] == potentialQuizzes[quiznum]:
                scores[quiz].append([line['score'], round(line['percentage'])])
            quiznum+=1
    print(scores)


presentScoreHistory(
    "scorehistory.json", 
    [
        "What Colour is That?", 
        "Tiers of Colours!", 
        "Fun with Colour Relationships!", 
        "Understanding Hue, Saturation and Value"
    ]
        )
