import numpy as np
import threading
import os


from game import ConnectFour
from game import simulate

import warnings
warnings.filterwarnings("error")



simulationThread = threading.Thread(target=simulate.simulate, args=())
simulationThread.start()
ConnectFour.main() #Starts the game ui
np.set_printoptions(edgeitems=30, linewidth=100000)
