import pandas as pd
from pandas import DataFrame


def rps():
    """
    Rock-Paper-Scissors game
    """
    probability_list = pd.DataFrame()
    USER_PREDICTION = ''
    while USER_PREDICTION != 'stop':
        USER_PREDICTION = raw_input('Input rock, paper, scissors: ').lower()
        probability_list.append(USER_PREDICTION)
        print probability_list


def conditional_probability_calc(prediction):
    """
    Convert predictions list to DataFrame and calculate the conditional
    probability of the next choice
    """

    conditional_probability_1 = []
    if prediction[-1] == 1:
        for i, j in enumerate(prediction):
            if j == 1:
                conditional_probability_1.append(prediction[i+1])
                print i, j, conditional_probability_1

    #     next_choice_prob = pd.DataFrame(prediction, columns=['selection'])
    #     return next_choice_prob.groupby('selection').size().div(len(next_choice_prob)).idxmax()
    # elif prediction(-1) == 2:
    #     return next_choice_prob.groupby('selection').size().div(len(next_choice_prob)).idxmax()
    # else:
    #     return next_choice_prob.groupby('selection').size().div(len(next_choice_prob)).idxmax()




if __name__ == '__main__':
    test = [1, 2, 3, 1, 2, 3, 2, 3, 2, 1, 2, 1, 2, 3, 2, 1]
    conditional_probability_calc(test)
