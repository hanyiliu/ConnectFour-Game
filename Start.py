import numpy as np
import threading
import os


from game import ConnectFour
from game import simulate

import warnings
warnings.filterwarnings("error")

##################################################################
#       Plan of attack:
#           - run game i times
#           - after i iterations, feed data into network
#           - train both players, but with differing values
#           - after training completes, repeat overall loop
#       - then itll all magically work right
#       TODO: include randomization if needed
#
#       Alternate plan of attack:
#           - get feedback from game (reinforced learning)
#           - add data to dataset for every time player connets three or four slots (add multiple examples of same value to create bias)
##################################################################


simulationThread = threading.Thread(target=simulate.simulate, args=())
simulationThread.start()
ConnectFour.main() #Starts the game ui
np.set_printoptions(edgeitems=30, linewidth=100000)
