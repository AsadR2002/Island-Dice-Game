'''
Name: Asad Rehman
Date: May 22 2019
File Name: IslandDice.py
Description: Simulates IslandDice Roll game. 
'''
def random_dice(): #Simulates Dice roll, returning value between 1 and 12
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    dsum = d1 + d2
    return dsum
def high_low(dsum, uguess): #User geusses if roll is high or low: The program takes their response and checks if it matches the outcome 
    dstatus = ""
    uguess_status = ""
    dmessage = ""
    if 2 <= dsum <= 6: #Sets parameters of low roll
        dstatus = "low"
        dmessage = "The dice rolled is low."
    elif 8 <= dsum <= 12: #Sets parameters of high roll
        dstatus = "high"
        dmessage = "The dice rolled is high."
    elif dsum == 7: #Seven is neither high or low, so it is always incorrect
        dmessage = "The dice rolled is a 7, neither high nor low."
        uguess_status = "Incorrect"
    if uguess == dstatus: #If it does match
        uguess_status = "Correct"
    elif uguess != dstatus: #If it does not match
        uguess_status = "Incorrect"
    return dstatus, uguess_status, dmessage
def total_shells(nshells, riskshells, uguess_status):
    gmessage = ""
    if uguess_status == "Correct":
        nshells += 2*riskshells
        gmessage = "Congratulations, you guessed correctly! You have won " + str(2*riskshells) + " shells!" #If correct, they gain 2x the shells they risked 
    elif uguess_status == "Incorrect":
        nshells -= riskshells
        gmessage = "Sorry, you guessed incorrectly! You have lost " + str(riskshells) + " shells!" #If incorrect, they lose the number of shells they risked 
    return nshells, gmessage
import random
print("Welcome to the Island dice program.") #Welcome 
def mainMenu():
    b = input("Please type one of the following in order to take an action: S - Start, H - Help, Q - Quit: ") #Option menu
    if b == 's' or b == 'S':#Start Game 
        nshells = 1000 #Start with 1000 shells 
        while nshells > 0: #If the number of shells falls to zero or below, the game ends 
            print("You have a total of " + str(nshells) + " shells.")
            risk_shells = nshells + 1
            while risk_shells > nshells:
                try:
                    risk_shells = int(input("Please type the number of shells you would like to risk: "))
                    if risk_shells > nshells: #You cannot risk more shells than you have 
                        print("You cannot risk more shells than you currently have. ")
                except ValueError:
                    print("Invalid input. Please enter an integer. ")
            uguess = input('Do you believe the dice rolled is a high or low number?("high: or "low")": ') #They guess if roll is high or low
            while uguess not in ("high","low"): #They must guess either high or low
                uguess = input("Sorry. Please choose either high or low. ")
            drolled = random_dice()
            dstatus, uguess_status, dmessage = high_low(drolled, uguess)
            nshells, gmessage = total_shells(nshells, risk_shells, uguess_status)
            print("The dice rolled is " + str(drolled) + ".") #Informs user of the value of the dice rolled 

        print("Sorry, you have lost all of your shells.")  
        print("GAME OVER. BETTER LUCK NEXT TIME!") #Game over once all shells are lost 
        input("Press the enter button to return to the main menu. ") 
        mainMenu()
    elif b == 'h' or b == 'H': #Explains Game 
        input('''In the Island Dice Roll game, you begin with 1000 shells.
              You are prompted for the number of shells to risk and a second prompt asks you to choose either high or low.
              The program simulates the rolling of two dice and the results are added together, and the outcome is compared to your choice of high or low.
              If the dice total is between 2 and 6 inclusive, then it is considered low.
              A total between 8 and 12 inclusive is high. A total of 7 is neither high nor low, and you lose the shells at risk.
              If you call correctly, the shells at risk are doubled and added to the total shells. For a wrong call, the player loses the shells at risk.
              The game ends once the player is out of shells.''')
        mainMenu()
    elif b == 'q' or b == 'Q':
        quit
    else:
        print("Invalid choice.")
        mainMenu()
mainMenu()

