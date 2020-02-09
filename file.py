#Dealing with files
def main():
    f=open('texts.txt')
    for text in f:
        print(text,end=" ")

main()