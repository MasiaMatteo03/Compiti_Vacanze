def last_added_score(list_scores):
    return list_scores[-1]

def high_score(list_scores):
    return max(list_scores)

def three_high_score(list_scores):
    cont = 0
    list_high = []
    while cont < 3:
        list_high.append(max(list_scores))
        list_scores.remove(max(list_scores))
        cont += 1
    
    print(f"The three high scores are: {list_high[0]}, {list_high[1]}, {list_high[2]}\n")
    

def main():
    list_score = [5, 2, 8, 7, 3]

    print(f"The last added score is: {last_added_score(list_score)}\n")
    
    print(f"The high score is: {high_score(list_score)}\n")

    three_high_score(list_score)

if __name__ == "__main__":
    main()