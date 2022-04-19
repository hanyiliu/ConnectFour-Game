import numpy as np
import Config
from game import check


def hypothesis(board):
    scores = check.check_all(np.copy(board), Config.opponentValue, connect_four_score=10)
    opponent_scores = check.check_all(np.copy(board), Config.playerValue, connect_four_score=7)

    opponent_scores[opponent_scores<4] = 0
    scores = scores + opponent_scores*0.5
    #print("hypothesis: {}".format(scores))
    return scores
