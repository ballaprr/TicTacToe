import random
# Author: Rohan Ballapragada
# 12/8/19

def get_player_piece():
    while(True):
        P1 = str(input("Player 1: What is your letter? ")) # Player selects their game piece
        P2 = str(input("Player 2: What is your letter? "))
        if P1 == P2:
            print("Error: Cannot have the same letter") # Can't have same game piece
        else:
            break

    return P1, P2

def main():
    P1, P2 = get_player_piece() 
    b = [[' ', " ", " "], # Empty game board
        [" ", " ", " "], 
        [" ", " ", " "]]
    choosePlayerCount(b, P1, P2)

def choosePlayerCount(b, P1, P2):
    a = int(input("Enter number: 1 Player or 2 Player ")) # One or two players
    if a == 2:
        TwoPlayer(b, P1, P2) # Two Player Game
    elif a == 1:
        OnePlayer(b, P1, P2) # One Player Game
    else:
        print("Error: Needs to be one or two")
        choosePlayerCount(b, P1, P2)

def OnePlayer(b, P1, P2):
    while True:
        while True:
            location1 = input("Player1: Where would you like to place your marker? ") # Location to place marker
            try:
                i = int(location1.split(' ')[0]) # Row
                j = int(location1.split(' ')[1]) # Column
                if (i >=0 and i<3 and j >= 0 and j < 3): # Error Catch
                    if (b[i][j]==' '):
                        b[i][j] = P1
                        break
                    else:
                        print('That location is currently occupied')
                else:
                    print("Location has to be within 0 0 and 2 2")
            except:
                print("Please Enter location in the format 0 0, 1 1")
        ind1 = location1.split(" ")
        b[int(ind1[0])][int(ind1[1])] = P1
        print_board(b)
        if is_winner(b, P1, P2) == True:
            break
        
        while True:
                i = int(random.random()*3) # Random number between 0 and 2
                j = int(random.random()*3)
                if (i >= 0 and j < 3 and i >= 0 and j < 3): #Error Catch
                    if (b[i][j] == ' '):
                        b[i][j] = P2
                        print('Player 2 selected the location: ',i,' ',j)
                        break
        print_board(b)
        if is_winner(b, P1, P2) == True:
            break

def TwoPlayer(b, P1, P2):
    while True:
        while True:
            location1 = input("Player1: Where would you like to place your marker? ") # Location for input
            try: 
                i = int(location1.split(' ')[0]) # Row
                print("i " + str(i))
                j = int(location1.split(' ')[1]) # Column
                print("j " + str(j))
                print(str(i) + ":" + str(j))
                if (i >=0 and i<3 and j >= 0 and j < 3): # Error Catch
                    if (b[i][j]==' '):
                        b[i][j] = P1
                        break
                    else:
                        print('That location is currently occupied')
                else:
                    print("Location has to be within 0 0 and 2 2")
            except:
                print("Please Enter location in the format 0 0, 1 1")
        ind1 = location1.split(" ")
        b[int(ind1[0])][int(ind1[1])] = P1
        print_board(b)
        if is_winner(b, P1, P2) == True:
            break
        while True:
            location2 = input("Players2: What would you like to place your marker? ") # Location for input
            try:
                i = int(location2.split(' ')[0]) # Row
                print("i " + str(i))
                j = int(location2.split(' ')[1]) # Column
                print("j " + str(j))
                print(str(i) + ":" + str(j))
                if (i >=0 and i<3 and j >= 0 and j < 3): # Error Catch
                    if (b[i][j]==' '):
                        b[i][j] = P2
                        break
                    else:
                        print('That location is currently occupied')
                else:
                    print("Location has to be within 0 0 and 2 2")
            except:
                print("Please Enter location in the format 0 0, 1 1")
        ind2 = location2.split(" ")
        b[int(ind2[0])][int(ind2[1])] = P2
        print()
        print_board(b)
        if is_winner(b, P1, P2) == True:
            break


def is_winner(b, P1, P2): # Method to Check Winner
    check = False
    count = 0
    for i in range (3):
        if (b[i][0] == b[i][1] == b[i][2] == P1): # Matching row Player 1
            check = True
            print("Player 1 is the winner!")
        elif (b[i][0] == b[i][1] == b[i][2] == P2): # Matching row Player 2
            check = True
            print("Player 2 is the winner!")
        elif (b[0][i] == b[1][i] == b[2][i] == P1): # Matching column Player 1
            check = True
            print("Player 1 is the winner!")
        elif (b[0][i] == b[1][i] == b[2][i] == P2): # Matching column Player 2
            check = True
            print("Player 2 is the winner")
    if (b[0][0] == b[1][1] == b[2][2] == P1): # Matching diagonal Player 1
        check = True
        print("Player 1 is the Winner")
    if (b[2][0] == b[1][1] == b[0][2] == P1): # Matching diagonal Player 1
        check = True
        print("Player 1 is the winner")
    if (b[0][0] == b[1][1] == b[2][2] == P2): # Matching diagonal Player 2
        check = True
        print("Player 2 is the Winner")
    if (b[2][0] == b[1][1] == b[0][2] == P2): # Matching diagonal Player 2
        check = True
        print("Player 2 is the winner")
    for i in range (3): # Checks tie
        for j in range (3):
            if (b[i][j] == P1):
                count = count + 1
            elif (b[i][j] == P2):
                count = count + 1
    if count == 9:
        check = True
        print("Tie game: Table is Full")
    return check

def print_board(b):
    for i in range (3):
        print(b[i][0], "|", b[i][1], "|", b[i][2])
        if (i < 2):
            print("----------")

main()