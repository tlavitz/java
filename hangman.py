import random
HANGMAN=("""
------
|    |
|
|
|
|
|
|
|
----------
""",
"""
------
|    |
|    0
|
|
|
|
|
|
----------
""",
"""
------
|    |
|    0
|   -+-
|
|
|
|
|
----------
""",
"""
------
|    |
|    0
|  /-+-
|
|
|
|
|
----------
""",
"""
------
|    |
|    0
|  /-+-/
|
|
|
|
|
----------
""",
"""
------
|    |
|    0
|  /-+-/
|    |
|
|
|
|
----------
""",
"""
------
|    |
|    0
|  /-+-/
|    |
|    |
|   |
|   |
|
----------
""",
"""
------
|    |
|    0
|  /-+-/
|    |
|    |
|   | |
|   | |
|
----------


""")



MAX_MISTAKE=6
#max=len(HANGMAN)-1
#print(max)

WORDS=("college","python","programming","designer","mobile")

word=random.choice(WORDS) #the word to be guessed

guide="-"*len(word) #one dash for each letter in the word to be guessed

wrong=0  #set wrong of player

used=[] #letters already guessed

#main

print("Welcome to Hangman.. Ganbatte ne!")

#as long as the player cant get the right word and still have mistakes left
while wrong<MAX_MISTAKE and guide!=word:
    print(HANGMAN[wrong])
    print("\nLetters that you used so far: \n",used)
    print("\nThe word is:\n",guide)

    guess=input("\nEnter your guess: ")
    guess=guess.lower()

    while guess in used:
        print("you already tried the letter",guess)
        guess=input("\nEnter your guess: ")
        guess=guess.lower()

    used.append(guess)

    if guess in word:
        print("\nYes, {0} is in the word".format(guess))
        #create a new guide to include guess
        new=""
        for i in range(len(word)):
            if guess==word[i]:
                new+=guess
            else:
                new+=guide[i]
        guide=new
    else:
        print("\nSorry {} is not in the word.".format(guess))
        wrong+=1

    if wrong==MAX_MISTAKE:
        print()

