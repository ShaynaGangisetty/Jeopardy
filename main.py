from classes import player
#Begins code
def main():
print("Welcome to Jeopardy!\n")
number = 0
player_name = input("What is the name of your first player? ")
the_player1 = player(player_name,)
player_name = input("What is the name of your second player? ")
the_player2 = player(player_name)
playerList = [the_player1.name, the_player2.name]
board = resetBoard()
print("\nHello " + the_player1.name + " and " + the_player2.name + ",
welcome to Jeopardy.\n")
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
#Returns the player with the highest score, their score, and ranking of
players
def get_high_score(the_player1,the_player2,playerList):
if the_player1.score > the_player2.score:
print(the_player1.name + " currently has the high score of " +
str(the_player1.score) + " points.")
playerList.remove(the_player1.name)
playerList.insert(0,the_player1.name)
print("the current ranking is... ")
for ranking in range(0,len(playerList)):
print(str(ranking),playerList[ranking])
elif the_player1.score < the_player2.score:
print(the_player2.name + " currently has the high score of " +
str(the_player2.score) + " points.")
playerList.remove(the_player2.name)
playerList.insert(0,the_player2.name)
print("the current ranking is... ")
for ranking in range(0,len(playerList)):
print(str(ranking),playerList[ranking])
elif the_player1.score == the_player2.score:
print("Currently both players have the same score! There is no
ranking, both player have the score of " + str(the_player1.score) + "
points.")
#Resets the board back to start a new game
def resetBoard():
return
['100','101','102','103','104','200','201','202','203','204','300','301','
302','303','304','400','401','402',
'403','404','500','501','502','503','504']
#Prints the most updated version of the board
def printJeopardy(board):
print(' ' + "History" + ' | ' + "Spanish" + ' | ' + "Algebra" + ' | ' +
"Grammar" + ' | ' + "Science" + ' ')
print('---------+---------+---------+---------+---------')
print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2] +
' | ' + board[3] + ' | ' + board[4] + ' ')
print('---------+---------+---------+---------+---------')
print(' ' + board[5] + ' | ' + board[6] + ' | ' + board[7] +
' | ' + board[8] + ' | ' + board[9] + ' ')
print('---------+---------+---------+---------+---------')
print(' ' + board[10] + ' | ' + board[11] + ' | ' + board[12]
+ ' | ' + board[13] + ' | ' + board[14] + ' ')
print('---------+---------+---------+---------+---------')
print(' ' + board[15] + ' | ' + board[16] + ' | ' + board[17]
+ ' | ' + board[18] + ' | ' + board[19] + ' ')
print('---------+---------+---------+---------+---------')
print(' ' + board[20] + ' | ' + board[21] + ' | ' + board[22]
+ ' | ' + board[23] + ' | ' + board[24] + ' ')
#Ends the game
def
):
endGame(the_player1,the_player2,get_high_score,resetBoard,board,playerList
if board == resetBoard():
print("\n")
get_high_score(the_player1,the_player2,playerList)
print("Hope you enjoyed playing the game, byeeeeee!!!!")
else:
choice = input("Are you sure you would like to end the game, the
game isn't completed. Please type yes or no in lowercase letters with no
extra spaces. ")
if choice == "yes":
get_high_score(the_player1,the_player2,playerList)
print("Hope you enjoyed playing the Jeopardy Game!")
print("ADIOSSSSSSSSS!!")
quit()
elif choice == "no":
print("Please enjoy the rest of the game")
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
else:
print("Choose yes or no")
#Player can choose either what category they'd like to do, getting the
high score or ending the game
def
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame):
print("Below is list of categories you may choose from, you may type
'high score' to view the current ranking, or type 'end game' to end the
game. Please choose one of these options as you play. In order to play
this game successfully, please follow the directions carefully. When
inputing answers please type in lowercase letters without any extra spaces
unless told otherwise.\n")
printJeopardy(board)
choice = input("Which subject or action would you like to choose?
Please type in lowercase letters. ")
if choice == "high score":
print("")
get_high_score(the_player1,the_player2,playerList)
print("Lets continue the game\n")
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
elif choice == "history":
history(the_player1,the_player2,playerList,board,get_high_score)
elif choice == "algebra":
algebra(the_player1,the_player2, playerList, board, get_high_score)
elif choice == "spanish":
spanish(the_player1,the_player2,playerList,board,get_high_score)
elif choice == "science":
science(the_player1,the_player2,playerList,board,get_high_score)
elif choice == "grammar":
grammar(the_player1,the_player2, playerList,board,get_high_score)
elif choice == "end game":
endGame(the_player1,the_player2,get_high_score,resetBoard,board,playerList
)
#If player chooses category history
def history(the_player1,the_player2,playerList,board,get_high_score):
print("Welcome to the US Government section! You may choose from any of
the following values: 100, 200, 300, 400, 500. The higher the point value,
the harder your questions will be. Make sure you're typing everything the
exact way its written, with no extra spaces at the beginning or end, or
else you'll get it wrong.")
choice = input("Would you like to continue? Please type yes or no with
no space. ")
while choice == choice in
["yes","yesss","Yes","YES","yea","Yea","YEA"]:
playerTurn = input("Who's turn is to play? ")
if playerTurn == the_player1.name:
valueChoice = input(the_player1.name + " please choose a value.
")
while valueChoice == "100" and board[0] != "done":
question = input("The Legislative branch is made up the
house of reps and...?: ")
if question == "Senate" or "The Senate" or "senate":
the_player1.increaseScore(100)
print("\ncongratulations! you are correct!\n")
elif question != "Senate" or "The Senate" or "senate":
the_player1.decreaseScore(100)
print("\noh no, that is incorrect.\n")
print("Your score currently is " + str(the_player1.score))
board[0] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
while valueChoice == "200" and board[5] != "done":
question = input("What is it called when a president
cancles a proposed bill?: ")
if question == "Veto" or "veto":
the_player1.increaseScore(200)
print("\ncongratulations! you are correct!\n")
elif question != "Veto" or "veto":
the_player1.decreaseScore(200)
print("\noh no, that is incorrect.\n")
print("Your score currently is " +
str(the_player1.score))
board[5] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
while valueChoice == "300" and board[10] != "done":
question = input("How long does a senator's term last?
Type the number: ")
str(the_player1.score))
if question == "6":
the_player1.increaseScore(300)
print("\ncongratulations! you are correct!\n")
elif question != "6":
the_player1.decreaseScore(300)
print("\noh no, that is incorrect.\n")
print("Your score currently is " +
board[10] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
while valueChoice == "400" and board[15] != "done":
question = input("The Constitution was signed in what
year? 1747, 1787, or 1847: ")
if question == "1787":
the_player1.increaseScore(400)
print("\ncongratulations! you are correct!\n")
elif question != "1787":
the_player1.decreaseScore(400)
print("\noh no, that is incorrect.\n")
print("Your score currently is " +
str(the_player1.score))
board[15] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
while valueChoice == "500" and board[20] != "done":
question = input("What is the number of voting members
in the house? Type the number: ")
str(the_player1.score))
if question == "435":
the_player1.increaseScore(500)
print("\ncongratulations! you are correct!\n")
elif question != "435":
the_player1.decreaseScore(500)
print("\noh no, that is incorrect.\n")
print("Your score currently is " +
board[20] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
elif playerTurn == the_player2.name:
valueChoice = input(the_player2.name + " please choose a value.
")
while valueChoice == "100" and board[0] != "done":
question = input("The Legislative branch is made up the
house of reps and...?: ")
if question == "Senate" or "The Senate" or "senate":
the_player2.increaseScore(100)
print("\ncongratulations! you are correct!\n")
elif question != "Senate" or "The Senate" or "senate":
the_player2.decreaseScore(100)
print("\noh no, that is incorrect.\n")
print("Your score currently is " + str(the_player2.score))
board[0] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
while valueChoice == "200" and board[5] != "done":
question = input("What is it called when a president
cancels a proposed bill?: ")
if question == "Veto" or "veto":
str(the_player2.score))
the_player2.increaseScore(200)
print("\ncongratulations! you are correct!\n")
elif question != "Veto" or "veto":
the_player2.decreaseScore(200)
print("\noh no, that is incorrect.\n")
print("Your score currently is " +
board[5] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
while valueChoice == "300" and board[10] != "done":
question = input("How long does a senator's term last?
Type the number: ")
str(the_player2.score))
if question == "6":
the_player2.increaseScore(300)
print("\ncongratulations! you are correct!\n")
elif question != "6":
the_player2.decreaseScore(300)
print("\noh no, that is incorrect.\n")
print("Your score currently is " +
board[10] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
while valueChoice == "400" and board[15] != "done":
question = input("The Constitution was signed in what
year? 1747, 1787, or 1847: ")
if question == "1787":
the_player2.increaseScore(400)
print("\ncongratulations! you are correct!\n")
elif question != "1787":
the_player2.decreaseScore(400)
print("\noh no, that is incorrect.\n")
print("Your score currently is " +
str(the_player2.score))
board[15] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
while valueChoice == "500" and board[20] != "done":
question = input("What is the number of voting members
in the house? Type the number: ")
if question == "435":
the_player2.increaseScore(500)
print("\ncongratulations! you are correct!\n")
elif question != "435":
the_player2.decreaseScore(500)
print("\noh no, that is incorrect.\n")
print("Your score currently is " +
str(the_player2.score))
board[20] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
if choice == choice in ["no","NO","No","NOPE","no","no thank you"]:
print("Oh no, sorry to hear that")
choice = input("Would you like to choose another category?")
if choice == choice in
["yes","yesss","Yes","YES","yea","Yea","YEA"]:
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
elif choice != choice in ["no","NO","No","NOPE","no","no thank
you"]:
print("Sorry, thanks for playing!")
#If player chooses category spanish
def spanish(the_player1,the_player2,playerList,board,get_high_score):
print("\nYou're currently in the Spanish section of the game. For this
section, the rules are the following. You have to write the correctly
conjugated word that is seen in the parenthesis. If correct you gain a
certain amount of points, however if you are incorrect, you loose that
same number of points. You may choose from the following values:
100,200,300,400,500. \n")
choice = input("Would you like to continue? Please type yes or no with
no space. ")
while choice in ["yes","yesss","Yes","YES","yea","Yea","YEA"]:
playerTurn = input("\nWho's turn is to play? ")
if playerTurn == the_player1.name:
valueChoice = input(the_player1.name + " please choose a value.
")
if valueChoice == "100" and board[1] != "done":
print("Año pasado, my familia ________(ir) a las tiendas.")
question = input("What is the correct conjugation? ")
if question == "fue":
the_player1.increaseScore(100)
print("\ncongratulations! you are correct!\n")
else:
the_player1.decreaseScore(100)
print("\noh no, that is incorrect.\n")
print("Your score currently is " + str(the_player1.score))
board[1] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
elif valueChoice == "200" and board[6] != "done":
print("Mi amiga, Samantha está ___________(comer) en
Dominos. ")
question = input("What is the correct conjugation? ")
if question == "comiendo":
the_player1.increaseScore(200)
print("\ncongratulations! you are correct!\n")
else:
the_player1.decreaseScore(200)
print("\noh no, that is incorrect.\n")
print("Your score currently is " + str(the_player1.score))
board[6] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
elif valueChoice == "300" and board[11] != "done":
print("Para vive una vida sana, es importante
___________(hacer) ejercicios.")
question = input("What is the correct conjugation? ")
if question == "hace":
the_player1.increaseScore(300)
print("\ncongratulations! you are correct!\n")
else:
the_player1.decreaseScore300(300)
print("\noh no, that is incorrect.\n")
print("Your score currently is " + str(the_player1.score))
board[11] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
elif valueChoice == "400" and board[16] != "done":
print("_____ (tener) alegría! (Está un mandato)")
question = input("What is the correct conjugation? ")
if question == "ten":
the_player1.increaseScore(400)
print("\ncongratulations! you are correct!\n")
else:
the_player1.decreaseScore(400)
print("\noh no, that is incorrect.\n")
print("Your score currently is " + str(the_player1.score))
board[16] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
_________(estirarse)")
elif valueChoice == "500" and board[21] != "done":
print("Despues el ejercicio, es importante tu
question = input("What is the correct conjugation? ")
if question == "te estirar":
the_player1.increaseScore(500)
print("\ncongratulations! you are correct!\n")
else:
the_player1.decreaseScore(500)
print("\noh no, that is incorrect.\n")
print("Your score currently is " + str(the_player1.score))
board[21] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
elif playerTurn == the_player2.name:
valueChoice = input(the_player2.name + " please choose a value.
")
if valueChoice == "100" and board[1] != "done":
print("Año pasado, my familia ________(ir) a las tiendas.")
question = input("What is the correct conjugation? ")
if question == "fue":
the_player2.increaseScore(100)
print("\ncongratulations! you are correct!\n")
else:
the_player2.decreaseScore(100)
print("\noh no, that is incorrect.\n")
print("Your score currently is " + str(the_player2.score))
board[1] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
elif valueChoice == "200" and board[6] != "done":
print("Mi amiga, Samantha está ___________(comer) en
Dominos. ")
question = input("What is the correct conjugation? ")
if question == "comiendo":
the_player2.increaseScore(200)
print("\ncongratulations! you are correct!\n")
else:
the_player2.decreaseScore(200)
print("\noh no, that is incorrect.\n")
print("Your score currently is " + str(the_player2.score))
board[6] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
elif valueChoice == "300" and board[11] != "done":
print("Para vive una vida sana, es importante
___________(hacer) ejercicios.")
question = input("What is the correct conjugation? ")
if question == "hace":
the_player2.increaseScore(300)
print("\ncongratulations! you are correct!\n")
else:
the_player2.decreaseScore(300)
print("\noh no, that is incorrect.\n")
print("Your score currently is " + str(the_player2.score))
board[11] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
elif valueChoice == "400" and board[16] != "done":
print("_____ (tener) alegría! (Está un mandato)")
question = input("What is the correct conjugation? ")
if question == "ten":
the_player2.increaseScore(400)
print("\ncongratulation!s")
else:
the_player2.decreaseScore(400)
print("\noh no, that is incorrect.\n")
print("Your score currently is " + str(the_player2.score))
board[16] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
elif valueChoice == "500" and board[21] != "done":
print("Despues el ejercicio, es importante tu
_________(estirarse)")
question = input("What is the correct conjugation? ")
if question == "te estirar":
the_player2.increaseScore(500)
print("\ncongratulations! you are correct!\n")
else:
the_player2.decreaseScore(500)
print("\noh no, that is incorrect.\n")
print("Your score currently is " + str(the_player2.score))
board[21] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
if choice == choice in ["no","NO","No","NOPE","no","no thank you"]:
print("Oh no, sorry to hear that :(")
choice = input("Would you like to choose another category?")
if choice == choice in
["yes","yesss","Yes","YES","yea","Yea","YEA"]:
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
elif choice == choice in ["no","NO","No","NOPE","no","no thank
you"]:
print("Sorry, thanks for playing!")
#If player chooses category algebra
def algebra(the_player1,the_player2,playerList,board,get_high_score):
print("Welcome to the Algebra sections! You may choose from any of the
following values: 100, 200, 300, 400, 500. The higher the point value,
the harder your question will be. Make sure you're typing everything the
exact way its written, with no extra spaces at the beginning or ending, or
else you'll get it wrong.")
choice = input("Would you like to continue? Please type yes or no with
no space. ")
while choice in ["yes","yesss","Yes","YES","yea","Yea","YEA"]:
playerTurn = input("Who's turn is it to play? ")
if playerTurn == the_player1.name:
choice = input(the_player1.name + " please choose a value. ")
while choice == "100" and board[2] != "done":
print("Solve the equations (y = -3x+4 and y = 3x-2) for the
values of x and y.")
answer = input ("Enter your answer as a ordered pair with
no spaces. If there are no solutions, type 'nosolutions'.")
if answer == "(1,1)":
the_player1.increaseScore(100)
print("Congratulations, you got that correct!")
else:
the_player1.decreaseScore(100)
print("Sorry, that is incorrect.")
print("Your score is " + str(the_player1.score))
board[2] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,
get_high_score,endGame)
while choice == "200" and board[7] != "done":
print("Solve the equations (x-y = 3 and 7x-y = -3) for the
values of x and y.")
question = input ("Enter your answer as a ordered pair with
no spaces. If there are no solutions, type 'nosolutions'.")
if question == "(-1,-4)":
the_player1.increaseScore(200)
print("Congratulations, you got that correct!")
else:
the_player1.decreaseScore(200)
print("Sorry, that is incorrect")
print("Your score is " + str(the_player1.score))
board[7] = "done"
menu(the_player1,the_player2, playerList,printJeopardy,
board,get_high_score,endGame)
while choice == "300" and board[12] != "done":
print("Solve the equations (0 = -2y+10-6x and 14-22y = 18x)
for the values of x and y.")
question = input ("Enter your answer as a ordered pair with
no spaces. If there are no solutions, type 'nosolutions'.")
if question == "(2,-1)":
the_player1.increaseScore(300)
print("Congratualions, you got that correct!")
else:
the_player1.decreaseScore(300)
print("Sorry, that is incorrect")
print("Your score is" + str(the_player1.score))
board[12] = "done"
menu(the_player1,the_player2, playerList,printJeopardy,
board,get_high_score,endGame)
while choice == "400" and board[17] != "done":
print("Solve the equations (-5/7-11/7x = -y and 2y = 7+5x)
for the values of x and y.")
question = input ("Enter your answer as a ordered pair with
no spaces. If there are no solutions, type 'nosolutions'.")
if question == "(-3,-4)":
the_player1.increaseScore(400)
print("Congratulations, you got that correct!")
else:
the_player1.decreaseScore(400)
print("Sorry, that is incorrect")
print("Your score is," + str(the_player1.score))
board[17] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
while choice == "500" and board [22] != "done":
print("Solve the equations (5x+5y+5z = -20, 4x+3y+3z = -6,
and -4x+3y+3z = 9) for the values of x and y.")
question = input ("Enter your answer as a ordered pair with
no spaces. If there are no solutions, type 'nosolutions'.")
if question == "nosolutions":
the_player1.increaseScore(500)
print("Contratulations, you got that correct!")
else:
the_player1.decreaseScore(500)
print("Sorry, that is incorrect")
print("Your score is, " + str(the_player1.score))
board[22] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
if playerTurn == the_player2.name:
choice = input(the_player2.name + " please choose a value. ")
while choice == "100" and board[2] != "done":
print("Solve the equations (y = -3x+4 and y = 3x-2) for the
values of x and y.")
question = input ("Enter your answer as a ordered pair with
no spaces. If there are no solutions, type 'nosolutions'.")
if question == "(1,1)":
the_player2.increaseScore(100)
print("Congratulations, you got that correct!")
board[2] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
else:
the_player2.decreaseScore(100)
print("Sorry, that is incorrect.")
print("Your score is " + str(the_player2.score))
board[2] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
while choice == "200" and board[7] != "done":
print("Solve the equations (x-y = 3 and 7x-y = -3) for the
values of x and y.")
question = input ("Enter your answer as a ordered pair with
no spaces. If there are no solutions, type 'nosolutions'.")
if question == "(-1,-4)":
the_player2.increaseScore(200)
print("Congratulations, you got that correct!")
else:
the_player2.decreaseScore(200)
print("Sorry, that is incorrect")
print("Your score is " + str(the_player2.score))
board[7] = "done"
menu(the_player1,the_player2, playerList,printJeopardy,
board,get_high_score,endGame)
while choice == "300" and board[12] != "done":
print("Solve the equations (0 = -2y+10-6x and 14-22y = 18x)
for the values of x and y.")
question = input ("Enter your answer as a ordered pair with
no spaces. If there are no solutions, type 'nosolutions'.")
if question == "(2,-1)":
the_player2.increaseScore(300)
print("Congratualions, you got that correct!")
else:
the_player2.decreaseScore(300)
print("Sorry, that is incorrect")
print("Your score is" + str(the_player2.score))
board[12] = "done"
menu(the_player1,the_player2, playerList,printJeopardy,
board, get_high_score,endGame)
while choice == "400" and board[17] != "done":
print("Solve the equations (-5/7-11/7x = -y and 2y = 7+5x)
for the values of x and y.")
question = input ("Enter your answer as a ordered pair with
no spaces. If there are no solutions, type 'nosolutions'.")
if question == "(-3,-4)":
the_player2.increaseScore(400)
print("Congratulations, you got that correct!")
else:
the_player2.decreaseScore(400)
print("Sorry, that is incorrect")
print("Your score is," + str(the_player2.score))
board[17] = "done"
menu(the_player1,the_player2,printJeopardy,playerList,board,
get_high_score,endGame)
while choice == "500" and board [22] != "done":
print(board[22])
print("Solve the equations (5x+5y+5z = -20, 4x+3y+3z = -6,
and -4x+3y+3z = 9) for the values of x and y.")
question = input ("Enter your answer as a ordered pair with
no spaces. If there are no solutions, type 'nosolutions'.")
if question == "nosolutions":
the_player2.increaseScore(500)
print("Contratulations, you got that correct!")
else:
the_player2.decreaseScore(500)
print("Sorry, that is incorrect")
print("Your score is, " + str(the_player2.score))
board[22] = "done"
menu(the_player1,the_player2,playerList,board,printJeopardy,get_high_score
,endGame)
#If player chooses category grammar
def grammar(the_player1,the_player2,playerList,board,get_high_score):
print("Welcome to the Grammar section! The objective is to Fix the
Grammar mistakes in the sentences that you receive. The higher point value
you choose, the harder your question will be. If you get it right, then
you get those many points added to your score. If you get it wrong, that
many points are subtracted from your score. You may choose from the
following values: 100, 200, 300, 400, 500. Make sure you're typing
everything the exact way its written, with no extra spaces at the
beginning or end, or else you'll get it wrong. ")
choice = input("Would you like to begin. Type yes or no. ")
while choice in ["Yes", "YES", "yes"]:
playerTurn = input("Who's turn is it to play? ")
if playerTurn == the_player1.name:
valueChoice = input(the_player1.name + " please choose a value.
")
if valueChoice == "100" and board[3] != "done":
print("")
valueChoice = input("We sometimes has tornadoes. ")
if valueChoice == "We sometimes have tornadoes.":
print("\nThat's right!")
the_player1.increaseScore(100)
else:
print("\nSorry, that is incorrect")
the_player1.decreaseScore(100)
print("Your score currently is " + str(the_player1.score))
board[3] = "done"
print("\n")
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
, endGame)
if valueChoice == "200" and board[8] != "done":
print("")
valueChoice = input("He telled me a story. ")
if valueChoice == "He told me a story.":
print("\nThat's right!")
the_player1.increaseScore(200)
else:
print("\nSorry, that is incorrect")
the_player1.decreaseScore(200)
print("Your score currently is " + str(the_player1.score))
board[8] = "done"
print("\n")
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
, endGame)
if valueChoice == "300" and board[13] != "done":
print("")
valueChoice = input("He ran quick to his car. ")
if valueChoice == "He ran quickly to his car.":
print("\nThat's right!")
the_player1.increaseScore(300)
else:
print("\nSorry, that is incorrect")
the_player1.decreaseScore(300)
print("Your score currently is " + str(the_player1.score))
board[13] = "done"
print("\n")
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
, endGame)
if valueChoice == "400" and board[18] != "done":
print("")
valueChoice = input("Their was something in the box.")
if valueChoice == "There was something in the box.":
print("\nThat's right!")
the_player1.increaseScore(400)
else:
print("\nSorry, that is incorrect")
the_player1.decreaseScore(400)
print("Your score currently is " + str(the_player1.score))
board[18] = "done"
print("\n")
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
, endGame)
if valueChoice == "500" and board[23] != "done":
print("")
valueChoice = input("I looked at me in the mirror. ")
if valueChoice == "I looked at myself in the mirror.":
print("\nThat's right!")
the_player1.increaseScore(500)
else:
print("\nSorry, that is incorrect")
the_player1.decreaseScore(500)
print("Your score currently is " + str(the_player1.score))
board[23] = "done"
print("\n")
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
, endGame)
elif playerTurn == the_player2.name:
valueChoice = input(the_player2.name + " please choose a value.
")
if valueChoice == "100" and board[3] != "done":
print("")
valueChoice = input("We sometimes has tornadoes. ")
if valueChoice == "We sometimes have tornadoes.":
print("\nThat's right!")
the_player2.increaseScore(100)
else:
print("\nSorry, that is incorrect")
the_player2.decreaseScore(100)
print("Your score currently is " + str(the_player2.score))
board[3] = "done"
print("\n")
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
, endGame)
if valueChoice == "200" and board[8] != "done":
print("")
valueChoice = input("He telled me a story. ")
if valueChoice == "He told me a story.":
print("\nThat's right!")
the_player2.increaseScore(200)
else:
print("\nSorry, that is incorrect")
the_player2.decreaseScore(200)
print("Your score currently is " + str(the_player2.score))
board[8] = "done"
print("\n")
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
, endGame)
if valueChoice == "300" and board[13] != "done":
print("")
valueChoice = input("He ran quick to his car. ")
if valueChoice == "He ran quickly to his car.":
print("\nThat's right!")
the_player2.increaseScore(300)
else:
print("\nSorry, that is incorrect")
the_player2.decreaseScore(300)
print("Your score currently is " + str(the_player2.score))
board[13] = "done"
print("\n")
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
, endGame)
if valueChoice == "400" and board[18] != "done":
print("")
valueChoice = input("Their was something in the box. ")
if valueChoice == "There was something in the box.":
print("\nThat's right!")
the_player2.increaseScore(400)
else:
print("\nSorry, that is incorrect")
the_player2.decreaseScore(400)
print("Your score currently is " + str(the_player2.score))
board[18] = "done"
print("\n")
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
, endGame)
if valueChoice == "500" and board[23] != "done":
print("")
valueChoice = input("I looked at me in the mirror. ")
if valueChoice == "I looked at myself in the mirror.":
print("\nThat's right!")
the_player2.increaseScore(500)
else:
print("\nSorry, that is incorrect")
the_player2.decreaseScore(500)
print("Your score currently is " + str(the_player2.score))
board[23] = "done"
print("\n")
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
, endGame)
else:
print("That person is not currently in the game")
if choice == choice in ["no","NO","No"]:
print("Oh no, sorry to hear that")
choice = input("Would you like to choose another category?")
if choice == choice in ["yes","Yes","YES"]:
menu(the_player1,the_player2,playerList, printJeopardy,board,
get_high_score, endGame)
elif choice == choice in ["no","NO","No"]:
print("Sorry, thanks for playing!")
quit()
#If player chooses category science
def science(the_player1,the_player2,playerList,board,get_high_score):
print("Welcome to the Science section! This involves mainly biology and
chemistry. You may choose from any of the following values: 100, 200, 300,
400, 500. The higher the point value, the harder your question will be. If
your answer is incorrect, you'll lose the same number of points you would
have gained if you had gotten the question correct. Make sure you're
typing everything the exact way its written, with no extra spaces at the
beginning or ending, or else you'll get it wrong.")
toplay = input("Would you like to begin? Type 'Yes' or 'No. ")
if toplay == "Yes":
print("Okay, let's begin!")
playerTurn = input("Who's turn is it to play?")
if playerTurn == the_player1.name:
option = int(input(the_player1.name + " please choose a value.
"))
while option == 100 and board[4] != "done":
question1 = int(input("How many single chromosomes do
humans have in each cell? Type only the number: "))
if question1 == 46:
print("You got it! That's correct! ")
the_player1.score = the_player1.score + 100
print("Your score is",the_player1.score)
board[4] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
else:
print("That's incorrect. Good luck on the next one!")
the_player1.score = the_player1.score - 100
print("Your score is",the_player1.score)
board[4] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
while option == 200 and board[9] != "done":
question2 = input("What is the substance whose solid state
can float on its liquid state? ")
if question2 in ["Water","water","H20"]:
print("You got it! That's correct! ")
the_player1.score = the_player1.score + 200
print("Your score is",the_player1.score)
board[9] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
else:
print("That's incorrect. Good luck on the next one!")
the_player1.score = the_player1.score - 200
print("Your score is",the_player1.score)
board[9] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
while option == 300 and board[14] != "done":
question3 = input("What organelle is responsible for
protein synthesis in the cell?" )
if question3 in ["Ribosome","ribosome"]:
print("You got it! That's correct! ")
the_player1.score = the_player1.score + 300
print("Your score is",the_player1.score)
board[14] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
else:
print("That's incorrect. Good luck on the next one!")
the_player1.score = the_player1.score - 300
print("Your score is",the_player1.score)
board[14] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
while option == 400 and board[19] != "done":
question4 = input("What are elements that have the same
number of protons but have different numbers of neutrons?")
if question4 in
["Isotope","isotope","Isotopes","isotopes"]:
print("You got it! That's correct! ")
the_player1.score = the_player1.score + 400
print("Your score is",the_player1.score)
board[19] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
else:
print("That's incorrect. Good luck on the next one!")
the_player1.score = the_player1.score - 400
print("Your score is",the_player1.score)
board[19] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
while option == 500 and board[24] != "done" :
question5 = input("What element on the periodic table has
27 protons?")
if question5 in ["Co","Cobalt","cobalt"]:
print("You got it! That's correct! ")
the_player1.score = the_player1.score + 500
print("Your score is",the_player1.score)
board[24] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
else:
print("That's incorrect. Good luck on the next one!")
the_player1.score = the_player1.score - 500
print("Your score is",the_player1.score)
board[24] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
elif playerTurn == the_player2.name:
option = int(input(the_player2.name + " please choose a value.
"))
while option == 100 and board[4] != "done":
question1 = int(input("How many single chromosomes do
humans have in each cell? Type only the number: "))
if question1 == 46:
print("You got it! That's correct! ")
the_player2.score = the_player2.score + 100
print("Your score is",the_player2.score)
board[4] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,
board, get_high_score,endGame)
else:
print("That's incorrect. Good luck on the next one!")
the_player2.score = the_player2.score - 100
print("Your score is",the_player2.score)
board[4] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,
board, get_high_score,endGame)
while option == 200 and board[9] != "done":
question2 = input("What is the substance whose solid state
can float on its liquid state? ")
if question2 in ["Water","water","H20"]:
print("You got it! That's correct! ")
the_player2.score = the_player2.score + 200
print("Your score is",the_player2.score)
board[9] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,get_high_score
,endGame)
else:
print("That's incorrect. Good luck on the next one!")
the_player2.score = the_player2.score - 200
print("Your score is",the_player2.score)
board[9] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,
board, get_high_score,endGame)
while option == 300 and board[14] != "done":
question3 = input("What organelle is responsible for
protein synthesis in the cell?" )
if question3 in ["Ribosome","ribosome"]:
print("You got it! That's correct! ")
the_player2.score = the_player2.score + 300
print("Your score is",the_player2.score)
board[14] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,
board, get_high_score,endGame)
else:
print("That's incorrect. Good luck on the next one!")
the_player2.score = the_player2.score - 300
print("Your score is",the_player2.score)
board[14] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,
board, get_high_score,endGame)
while option == 400 and board[19] != "done":
question4 = input("What are elements that have the same
number of protons but have different numbers of neutrons?")
if question4 in ["Isotope","isotope"]:
print("You got it! That's correct! ")
the_player2.score = the_player2.score + 400
print("Your score is",the_player2.score)
board[19] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,
board, get_high_score,endGame)
else:
print("That's incorrect. Good luck on the next one!")
the_player2.score = the_player2.score - 400
print("Your score is",the_player1.score)
board[19] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,
board, get_high_score,endGame)
while option == 500 and board[24] != "done" :
question5 = input("What element on the periodic table has
27 protons?")
if question5 in ["Co","Cobalt","cobalt"]:
print("You got it! That's correct! ")
the_player2.score = the_player2.score + 500
print("Your score is",the_player2.score)
board[24] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,board,
get_high_score,endGame)
else:
print("That's incorrect. Good luck on the next one!")
the_player2.score = the_player2.score - 500
print("Your score is",the_player2.score)
board[24] = "done"
menu(the_player1,the_player2,playerList,printJeopardy,
board, get_high_score,endGame)
elif toplay == "No":
then = print ("Would you like to choose another category? Yes or
No? ")
if then == Yes:
choice = input("What category would you like to play? Please
type in lowercase letters. ")
if then == No:
print ("Okay, thanks for playing!")
elif toplay != "Yes" and toplay != "No" :
print("Please say either 'Yes' or 'No'. Make sure you're using the
right capitilization.")
toplay = input("Would you like to begin? Type 'Yes' or 'No. ")
main()
