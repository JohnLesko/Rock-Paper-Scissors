# Standard module imports
import pandas as pd
import random

# External module imports
import constants


def rps(user_prediction):
    """
    Rock-Paper-Scissors game logic
    """
    if len(user_prediction) < 4:
        return random.randint(1, 3)
    else:
        if conditional_probability_calc(user_prediction) == 1:
            return "Paper"
        elif conditional_probability_calc(user_prediction) == 2:
            return "Scissors"
        else:
            return "Rock"


def conditional_probability_calc(prediction):
    """
    Convert predictions list to DataFrame and calculate the conditional
    probability of the next choice based on the
    """

    if prediction[-1] == 1:
        for i, j in enumerate(prediction):
            if (j == 1) and (len(prediction) != i+1):
                constants.CONDITIONAL_PROBABILITY_1.append(prediction[i+1])
        next_choice_prob = pd.DataFrame(constants.CONDITIONAL_PROBABILITY_1, columns=['selection'])
        return next_choice_prob.groupby('selection').size().div(len(next_choice_prob)).idxmax()
    elif prediction[-1] == 2:
        for i, j in enumerate(prediction):
            if (j == 2) and (len(prediction) != i+1):
                constants.CONDITIONAL_PROBABILITY_2.append(prediction[i+1])
        next_choice_prob = pd.DataFrame(constants.CONDITIONAL_PROBABILITY_2, columns=['selection'])
        return next_choice_prob.groupby('selection').size().div(len(next_choice_prob)).idxmax()
    else:
        for i, j in enumerate(prediction):
            if (j == 3) and (len(prediction) != i+1):
                constants.CONDITIONAL_PROBABILITY_3.append(prediction[i+1])
        next_choice_prob = pd.DataFrame(constants.CONDITIONAL_PROBABILITY_3, columns=['selection'])
        return next_choice_prob.groupby('selection').size().div(len(next_choice_prob)).idxmax()
