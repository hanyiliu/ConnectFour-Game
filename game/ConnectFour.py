from tkinter import *
from functools import partial
import numpy as np
import Config
import os

from game import check


size = [6,7] #rows, columns; i = row, j = column
rows = [] #2D array
buttons = []
board = np.zeros((6,7)) #2D array of board in numerical values #column, row
turn = 0 #0 = player 1, 1 = player 2
endStatus = True
displayWinner = None
running = True
ready = False

#Data storage
player1Data = ([],[]) #list of board values, choice
player2Data = ([],[]) #list of board values, choice


def getButtons():
    return buttons

def getBoard():
    return board

def getTurn():
    return turn

def getEndStatus():
    return endStatus
def setEndStatus(newStatus):
    global endStatus
    endStatus = newStatus

def inputStatus(status):
    for i in range(np.size(buttons)):
        if(status):
            buttons[i].config(state=NORMAL)
        else:
            buttons[i].config(state=DISABLED)


def move(column): #places piece in column
    global turn

    for i in range(size[0]-1,-1,-1): #reversed iteration because piece goes to bottom, not top lol
        if(rows[i][column].cget("disabledbackground") == "white"):
            if(turn == 0):
                #storing data
                player1Data[0].append(board.flatten())
                player1Data[1].append(column)

                #updating board
                rows[i][column].config(disabledbackground="red")
                board[i][column] = Config.playerValue
                turn = 1



            else:
                #storing data
                player2Data[0].append(board.flatten())
                player2Data[1].append(column)

                #updating board
                rows[i][column].config(disabledbackground="yellow")
                board[i][column] = Config.opponentValue
                turn = 0

            state = check.check(board,i,column)
            if state == 1:
                print("Player 1 Wins.")
                displayWinner.config(text="Winner: Player")
                inputStatus(False)
                setEndStatus(False)
            elif state == 2:
                print("Player 2 Wins.")
                displayWinner.config(text="Winner: Computer")
                inputStatus(False)
                setEndStatus(False)
            return

def reset():

    global board
    global turn
    global displayWinner
    global running

    for i in range(size[0]): #create each point on board
        for j in range(size[1]):
            rows[i][j].config(disabledbackground="white")
    board = np.zeros((6,7)) #2D array of board in numerical values #column, row
    turn = 0 #0 = player 1, 1 = player 2
    displayWinner.config(text="Winner: ")
    inputStatus(True)
    setEndStatus(True)



def on_closing():
    global running

    running = False
    root.destroy()


def main():

    global root
    global displayWinner
    global ready

    root = Tk()
    #create files for data storage (if not present)
    for i in range(size[0]): #create each point on board
        cols = []

        for j in range(size[1]):

            e = Entry(root,relief=GROOVE)

            e.grid(row=i, column=j, sticky=NSEW, padx=5, pady=5, ipadx=1, ipady=1)

            e.insert(END, '')

            e.config(width=2)

            e.config(disabledbackground="white")


            e.config(state=DISABLED)

            cols.append(e)

        rows.append(cols)


    for j in range(size[1]): #create button to place pieces

        b = Button(root,command=partial(move, j))

        b.grid(row=7, column=j, padx=5, pady=5, ipadx=10, ipady=10)

        buttons.append(b)


    r = Button(root,command=partial(reset))
    r.config(text="Reset")
    r.grid(row=8, column=7, padx=5, pady=5, ipadx=10, ipady=10)

    # rows[0][0].config(disabledbackground="purple");
    displayWinner = Label(root,text="Winner: ", justify="left", anchor="w")
    displayWinner.grid(row=8, columnspan=10, padx=20, pady=5, ipadx=10, ipady=10, sticky="w")

    #automated loops

    root.title("Connect Four")
    root.protocol("WM_DELETE_WINDOW", on_closing)
    ready = True
    root.mainloop()


# if __name__ == "__main__":
#     main()
