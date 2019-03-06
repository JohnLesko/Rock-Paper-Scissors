import pandas as pd
import constants


def rps(user_prediction):
    """
    Rock-Paper-Scissors game logic
    """
    if conditional_probability_calc(user_prediction) == 1:
        print 2
    elif conditional_probability_calc(user_prediction) == 2:
        print 3
    else:
        print 1


def conditional_probability_calc(prediction):
    """
    Convert predictions list to DataFrame and calculate the conditional
    probability of the next choice
    """

    if prediction[-1] == 1:
        for i, j in enumerate(prediction):
            if (j == 1) and (len(prediction) != i+1):
                constants.CONDITIONAL_PROBABILITY.append(prediction[i+1])
        next_choice_prob = pd.DataFrame(constants.CONDITIONAL_PROBABILITY, columns=['selection'])
        return next_choice_prob.groupby('selection').size().div(len(next_choice_prob)).idxmax()
    elif prediction[-1] == 2:
        for i, j in enumerate(prediction):
            if (j == 2) and (len(prediction) != i+1):
                constants.CONDITIONAL_PROBABILITY.append(prediction[i+1])
        next_choice_prob = pd.DataFrame(constants.CONDITIONAL_PROBABILITY, columns=['selection'])
        return next_choice_prob.groupby('selection').size().div(len(next_choice_prob)).idxmax()
    else:
        for i, j in enumerate(prediction):
            if (j == 3) and (len(prediction) != i+1):
                constants.CONDITIONAL_PROBABILITY.append(prediction[i+1])
        next_choice_prob = pd.DataFrame(constants.CONDITIONAL_PROBABILITY, columns=['selection'])
        return next_choice_prob.groupby('selection').size().div(len(next_choice_prob)).idxmax()
