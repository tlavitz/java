scores=[]
choice=""

while choice!="0":
    print("""
    High Scores

    0-Exit
    1-Show Scores
    2-Add a Score
    3-delete a score
    4-Sort Scores
    """)

    choice=input("Choice: ")
    print()

    if choice=="0":
        print("Bye")

    elif choice=="1":
        print("high Score")
        print(scores)
        #for score in scores:
            #print(score)

    elif choice=="2":
        score=int(input("What score did you get?"))
        scores.append(score)

    elif choice=="3":
        score=int(input("Remove what score?:" ))
        if score in scores:
            scores.remove(score)

        else:
            print(score,"isnt in the high scores list.")

    elif choice=="4":
        scores.reverse()

    else:
        print("invalid choice")







