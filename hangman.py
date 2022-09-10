from time import sleep 
import os 

word=input("Player 1 Enter your word: ")
newlist=list(word)
answer=["*"]*len(word)
tries=list("hangman")
index=0

print("Word disappears in 3 seconds:")
sleep(3)
os.system('clear')

print("Player 2 get ready to guess :)")

for item in range(0,len(word)):
    if word[item]==" ":
        answer[item]=" "

    
def check_word(guess):
    global index
    count=0
    for item in range(0,len(word)):
        if newlist[item]==guess:
            answer[item]=guess
            count=count+1

    if count==0:
        tries[index]="X"
        index=index+1
        
    print(answer)
    print("Available tries:")
    print(tries)
    print()
    flag=check_winner(answer,tries)
    
    if flag==2:
        print("Player 2 is the winner")
    elif flag==1:
        print("Player 1 is the winner")
    else:
        check_letter()
    

def check_letter():    
    guess=input("Enter your guess: ")
    
    if len(guess) > 1:
        print("Enter a single letter")
        check_letter()
    check_word(guess)


def check_winner(answer,tries):
    
    if answer==newlist:
        return 2
    if tries==["X"]*7:
        return 1

check_letter()
