import sys

def openFile(fileName,mode):
    try:
        quizFile=open(fileName,mode)
    except IOError as e:
        print("Unable to open the file",fileName,"Ending program.\n",e)
        input("Press any key to exit")
        sys.exit()
    else:
        return quizFile

def nextLine(quizFile):
    line=quizFile.readline()
    #line=line.replace("/","\n")
    return line

def next_block(quizFile):
    category=nextLine(quizFile)
    question=nextLine(quizFile)

    answers=[]
    for i in range(4):
        answers.append(nextLine(quizFile))

    correct=nextLine(quizFile)

    if correct:
        correct=correct[0]
    explanation=nextLine(quizFile)

    return category,question,answers,correct,explanation

def welcome(title):
    print("National Computer Center(NCC) Examination")
    print(title)

def main():
    trivia_file=openFile("trivia.txt","r")
    title=nextLine(trivia_file)
    welcome(title)
    score=0
    category,question,answers,correct,explanation=next_block(trivia_file)
    while category:
        print(category)
        print(question)
        for i in range(4):
            print("\t",i+1,"-",answers[i])


        #get answer
        answer=input("What is your answer?: ")

        if answer==correct:
            print("Right!")
            score+=1
        else:
            print("Wrong")
        print(explanation)
        print("Score:",score,"\n\n")

        #get next block
        category,question,answers,correct,explanation=next_block(trivia_file)



main()
input("\n\nPress any key to exit")