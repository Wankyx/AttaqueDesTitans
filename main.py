#coding:utf-8
import random 
import playsound 

def playerName(msg):
    dataInStreamOk = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN1234567890"
    correctInputStream = False 
    i = 0
    j = 0
    while not correctInputStream:
        name = input(msg)
        while i < len(name):
            while j < len(dataInStreamOk):
                if name[i] in dataInStreamOk:
                    correctInputStream = True
                else:
                    correctInputStream = False 
                    break # quit la boucle
                j += 1
            i +=1
            j = 0 
        if not correctInputStream:
            print("[*] Please enter text...")
            i = 0
            j = 0

    return name 

 
firstPlayerName = playerName("\t\t[+] Enter a first player name >\n\t\t\t\t\t\t")
secondPlayerName = playerName("\t\t[+] Enter a second player name >\n\t\t\t\t\t\t")

firstPlayerLife = 250
secondPlayerLife = 250 
thisRound = 0 
roundMax = 4 
turn = True 
domage = 0 

quit = False 

while not quit:
    print("==============================")
    print("=      PREPARE TO FIGHT      =")
    print("==============================")

    while thisRound < roundMax:
        thisRound+=1 
        if turn:
            print("[{}] press enter to fight. . .".format(firstPlayerName))
            input() 

            if random.randint(0, 1) == 0:
                print("\t\tYOU MISS !")
                domage = 0
            else:
                domage = random.randint(0, 100) 
                secondPlayerLife -= domage
            turn = False
            playsound.playsound("resources/hit2.mp3", True)
            print("The player {} send {} domage to {} .".format(firstPlayerName, domage, secondPlayerName))

        else:

            print("[{}] press enter to fight. . .".format(secondPlayerName))
            input() 
            if random.randint(0, 1) == 0:
                print("\t\tYOU MISS !")
                domage = 0
            else:
                domage = random.randint(0, 100) 
                firstPlayerLife -= domage
            turn = True 
            playsound.playsound("resources/hit1.mp3", True)
            print("The player {} send {} domage to {} .".format(secondPlayerName, domage, firstPlayerName))
    playsound.playsound("resources/win.mp3", True)

    if firstPlayerLife > secondPlayerLife:
        print("[+] The player {} win with {} health point.".format(firstPlayerName, firstPlayerLife))
    else:
        print("[+] The player {} win with {} health point.".format(secondPlayerName, secondPlayerLife))

    thisRound = 0

    readStreamQuitInput = input("\t\t\tDo you want quit ? (y/N)")
    
    if not readStreamQuitInput == "":
        quit = True 
 