import random
WORDS=("asia","europe","us")
#word=WORDS[random.randrange(len(WORDS))]
word=random.choice(WORDS)
answer=word
jumble=""
#print(word)
while word:
    position=random.randrange(len(word))
    jumble+=word[position]
    word=word[:position]+word[(position+1):]

#main
print("""
welcome to word jumble
unscramble the letters to make the right word
(enter quit to exit game)
""")
print("the jumble word is:", jumble)

guess=input("\nEnter your guess: ")
while guess!=answer and guess !="quit":
    print("Sorry, Guess again:")
    guess=input("Enter your guess: ")

if guess==answer:
    print("Thats right!! you got it! ")

print("Thanks for playing")