import random
import string

#the draw of a new hangman(start all over)
def draw_hangman():
    #the drawing of the hangman.
    IMG0 = '+----+\n' + \
           '     |\n' + \
           '________'

    IMG1='+----+\n'+ \
         '     []\n'+ \
         '      \n'+ \
         '      \n'+ \
         '________'
    IMG2 = '+----+\n' + \
           '     []\n' + \
           '      |\n' + \
           '      |\n' + \
           '________'
    IMG3 = '+----+\n' + \
           '     []\n' + \
           '      |\n' + \
           '      /\n' + \
           '________'
    IMG4 = '+----+\n' + \
           '     []\n' + \
           '      |\n' + \
           '      /\ \n' + \
           '________'
    IMG5 = '+----+\n' + \
           '     []\n' + \
           '     /\n' + \
           '      |\n' + \
           '     /\ \n' + \
           '________'
    IMG6 = '+----+\n' + \
           '     []\n' + \
           '     /\ \n' + \
           '      |\n' + \
           '     /\ \n' + \
           '________'
    IMG7 = '+----+\n' + \
           '     []\n' + \
           '     /\ \n' + \
           '      |\n' + \
           '     /\ \n' + \
           '    [] \n' + \
           '________'
    IMG8 = '+----+\n' + \
           '     []\n' + \
           '     /\ \n' + \
           '      |\n' + \
           '     /\ \n' + \
           '    [][]\n' + \
           '________'
    IMG9 = '+----+\n' + \
           '     []\n' + \
           '     /\ \n' + \
           '    []\n' + \
           '      |\n' + \
           '     /\ \n' + \
           '    [][]\n' + \
           '________'
    IMG10 = '+----+\n' + \
           '     []\n' + \
           '     /\ \n' + \
           '    [][]\n' + \
           '      |\n' + \
           '     /\ \n' + \
           '    [][]\n' + \
           '________'
    IMG11 = '+----+\n' + \
            '    [+ ]\n' + \
            '    [  ]\n' + \
            '     /\ \n' + \
            '    [][]\n' + \
            '      |\n' + \
            '     /\ \n' + \
            '    [][]\n' + \
            '________'
    IMG12 = '+----+\n' + \
            '    [+ +]\n' + \
            '    [   ]\n' + \
            '     /\ \n' + \
            '    [][]\n' + \
            '      |\n' + \
            '     /\ \n' + \
            '    [][]\n' + \
            '________'
    IMG13 = '+----+\n' + \
            '    [+ +]\n' + \
            '    [ * ]\n' + \
            '     /\ \n' + \
            '    [][]\n' + \
            '      |\n' + \
            '     /\ \n' + \
            '    [][]\n' + \
            '________'
    IMG14 = '+----+\n' + \
            '    [+ +]\n' + \
            '    [ * ]\n' + \
            '    [===]\n' + \
            '     /\ \n' + \
            '    [][]\n' + \
            '      |\n' + \
            '     /\ \n' + \
            '    [][]\n' + \
            '________'
    IMG15 = '+----+\n' + \
            '    [+ +]\n' + \
            '    [ * ]\n' + \
            '    [===]\n' + \
            '------------\n' + \
            '     /\ \n' + \
            '    [][]\n' + \
            '      |\n' + \
            '     /\ \n' + \
            '    [][]\n' + \
            '________'
    hangman=[IMG0,IMG1,IMG2,IMG3,IMG4,IMG5,IMG6,IMG7,IMG8,IMG9,IMG10,IMG11,IMG12,IMG13,IMG14,IMG15]
    return hangman
#the choosing of a word from large words file.#
def choose_random_word():
    myfile=open("words.txt")
    content=myfile.readlines()
    word=random.choice(content)
    myfile.seek(0)
    myfile.close()
    return word


def main():
    option = 1
    while option!=0:
        #choosing options:
        print("choose an option")
        print("1-versus computer")
        print("2-no rush its just you")
        print("0-end game")
        option=int(input())
        if(option==1):
             username = input("enter user name:")
             #counter will be for iteration of put letters inside!
             # the i will be for the hang man puppet to appear!
             # flag mark that not all the letters revealed.
             i=0
             flag=0
             cpuPoints=0
             userPoints=0
             winner=0
             letterflag=0
             counter=0
             blankWord=[]
             puppet=draw_hangman()
             myWord=choose_random_word()
             print(myWord)
             for ch in myWord.rstrip():
                 if (ch!=' '):
                     blankWord.append('_')
                 elif (ch==' '):
                     blankWord.append(' ')
                 else:
                     break
             print("\n")
             print(blankWord)
             print(puppet[i])
             while(i<15):
                 flag=0
                 letterflag=0
                 for x in blankWord:
                     if(x=='_'):
                         flag=1
                 if(flag==1):
                     counter = 0
                     character = input("please select character:")
                     for ch in myWord.rstrip():
                         if (ch == character):
                             blankWord[counter] = character
                             letterflag=1
                             userPoints+=1
                         counter += 1
                     if (letterflag == 0):
                         print("you are wrong!")
                         i += 1
                         userPoints-=1
                         print(puppet[i])
                     print("\n")
                     print(blankWord)
                     for x in blankWord:
                         if (x == '_'):
                             flag = 1
                     if (flag == 1):
                         counter=0
                         cpuLetter = random.choice(string.ascii_lowercase)
                         print(cpuLetter)
                         for ch in myWord.rstrip():
                             if (ch == cpuLetter):
                                 blankWord[counter] = cpuLetter
                                 letterflag = 1
                                 cpuPoints += 1
                             counter += 1
                         if (letterflag == 0):
                             print("CPU is wrong!")
                             i += 1
                             cpuPoints -= 1
                         print(puppet[i])
                         print("\n")
                         print(blankWord)
                 else:
                     if(userPoints>cpuPoints):
                         print("*****" + username + " have WON!!!*****")
                         break
                     else:
                         print("*****CPU WON,you`re HANG MAN!!!!!*****")
                         print("the word was " + myWord)
                         break
             print("thanks for playing!")
        elif(option==2):
            username = input("enter user name:")
            # counter will be for iteration of put letters inside!
            # the i will be for the hang man puppet to appear!
            # flag mark that not all the letters revealed.
            i = 0
            flag = 0
            winner = 0
            letterflag = 0
            counter = 0
            blankWord = []
            puppet = draw_hangman()
            myWord = choose_random_word()
            for ch in myWord.rstrip():
                if (ch != ' '):
                    blankWord.append('_')
                else:
                    blankWord.append(' ')
            print("\n")
            print(blankWord)
            print(puppet[i])
            while (i < 15):
                flag = 0
                letterflag = 0
                for x in blankWord:
                    if (x == '_'):
                        flag = 1
                if (flag == 1):
                    counter = 0
                    character = input("please select character:")
                    for ch in myWord.rstrip():
                        if (ch == character):
                            blankWord[counter] = character
                            letterflag = 1
                        counter += 1
                    if (letterflag == 0):
                        print("you are wrong!")
                        i += 1
                        print(puppet[i])
                    print("\n")
                    print(blankWord)
                else:
                    print("" + username + " have WON!!!")
                    winner = 1
                    break
            if (winner == 0):
                print("" + username + " have LOST!!!")
                print("the word was " + myWord)

        elif(option==0):

                print("you chosen 0 - quit game.\n")

        else:
            print("option not exist!\n")



if __name__ == '__main__':
    main()
