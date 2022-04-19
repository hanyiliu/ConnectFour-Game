from random import randrange
import time
import numpy as np
import statistics
import os

from game import ConnectFour
from game import manualBot
import Config

#Statistics


def simulate():

    while not ConnectFour.ready:
        time.sleep(0.1)
    buttons = ConnectFour.getButtons()
    print("beginning game")


    while ConnectFour.running:

        while not ConnectFour.getEndStatus():
            if not ConnectFour.running:
                break
            time.sleep(0.1)

        if ConnectFour.getTurn() == 1:

            scores = manualBot.hypothesis(ConnectFour.getBoard())
            guess = np.random.choice(np.flatnonzero(scores == scores.max()))
            buttons[guess].invoke()

        time.sleep(Config.waitTime)
