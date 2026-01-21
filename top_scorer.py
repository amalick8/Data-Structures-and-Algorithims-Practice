def top_scorer(names, scores):
    highest_score = scores[0]
    best_name = names[0]

    for i in range(len(scores)):
        if scores[i] > highest_score:
            highest_score = scores[i]
            best_name = names[i]
    return best_name
print(top_scorer(['Ammar','Malick'],[85,90]))