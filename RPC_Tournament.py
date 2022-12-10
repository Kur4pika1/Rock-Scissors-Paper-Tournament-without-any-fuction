import random


choices = ["R", "P", "S"]
playerList = []
winnerList = []

playerCount = int(input("player number=  "))

# adding players to player list
for i in range(0, playerCount):
    print(i + 1, "player name: ")
    player = input()
    playerList.append(player)

# control variable
control = 1
roundCount = 0

# stay in loop until find the winner
while len(playerList) > 1:

    # determine if a length of playList is odd or even
    if (len(playerList) % 2 == 0):
        control = 0
    else:
        control = 1

    roundCount = roundCount + 1
    print("Round", roundCount)
    # setting the matches for a round
    for i in range(0, int(len(playerList) / 2) + control):

        # when the playerList has one player moving the player to next round and break the loop
        # and to not break while loop moving winner players to playerList
        if (len(playerList)) == 1:
            print(playerList[0], "goes to upper bracket because there is no player to match")
            winnerList.append(playerList[0])
            playerList.remove(playerList[0])

            for x in winnerList:
                playerList.append(x)

            winnerList.clear()
            break

        print("match", i + 1)

        # choosing the players and their choices
        #Remowing players from playerList when players play their match
        f_p = random.choice(playerList)
        playerList.remove(f_p)
        s_p = random.choice(playerList)
        playerList.remove(s_p)
        f_p_c = random.choice(choices)
        s_p_c = random.choice(choices)

        # checking the choices if they are same
        while f_p_c == s_p_c:

            print("!!! Same choices. Rematching. First player choice :", f_p_c, "Second player choice :", s_p_c)
            f_p_c = random.choice(choices)
            s_p_c = random.choice(choices)

        

        # Setting winners of rock paper scissors       
        if f_p_c == "R":
            if s_p_c == "P":
                winnerList.append(s_p)
                print("Winner player :",s_p, " winner choice: ", s_p_c)
                print("Loser player: ", f_p, " loser choice: ", f_p_c)
            else:
                winnerList.append(f_p)
                print("Winner player :",f_p, " winner choice: ", f_p_c)
                print("Loser player: ", s_p, " loser choice: ", s_p_c)
        elif f_p_c == "P":
            if s_p_c == "S":
                winnerList.append(s_p)
                print("Winner player :",s_p, " winner choice: ", s_p_c)
                print("Loser player: ", f_p, " loser choice: ", f_p_c)
                      
            else:
                winnerList.append(f_p)
                print("Winner player :",f_p, " winner choice: ", f_p_c)
                print("Loser player: ", s_p, " loser choice: ", s_p_c)
        else:
            if s_p_c == "R":
                winnerList.append(s_p)
                print("Winner player :",s_p, " winner choice: ", s_p_c)
                print("Loser player: ", f_p, " loser choice: ", f_p_c)
            else:
                winnerList.append(f_p)
                print("Winner player :",f_p, " winner choice: ", f_p_c)
                print("Loser player: ", s_p, " loser choice: ", s_p_c)

        # When playerList is empty, moving the players to playerList from winnerList to start next round
        if (len(playerList) == 0):
            for x in winnerList:
                playerList.append(x)
            winnerList.clear()

#When playerList has only one player this player is the winner of tournament
print("Winner Player :", playerList[0])
