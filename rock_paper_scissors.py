import pandas as pd


def rps():
    """
    Rock-Paper-Scissors game
    """
    probability_list = pd.DataFrame()
    user_prediction = ''
    while user_prediction != 'stop':
        user_prediction = raw_input('Input rock, paper, scissors: ').lower()
        probability_list.append(user_prediction)
        print conditional_probability_calc(probability_list)


def conditional_probability_calc(prediction):
    """
    Convert predictions list to DataFrame and calculate the conditional
    probability of the next choice
    """

    conditional_probability = []

    if prediction[-1] == 1:
        for i, j in enumerate(prediction):
            if (j == 1) and (len(prediction) != i+1):
                conditional_probability.append(prediction[i+1])
                print i+1, len(prediction), j, conditional_probability
        next_choice_prob = pd.DataFrame(conditional_probability, columns=['selection'])
        return next_choice_prob.groupby('selection').size().div(len(next_choice_prob)).idxmax()
    elif prediction[-1] == 2:
        for i, j in enumerate(prediction):
            if (j == 2) and (len(prediction) != i+1):
                conditional_probability.append(prediction[i+1])
                print i+1, len(prediction), j, conditional_probability
        next_choice_prob = pd.DataFrame(conditional_probability, columns=['selection'])
        return next_choice_prob.groupby('selection').size().div(len(next_choice_prob)).idxmax()
    else:
        for i, j in enumerate(prediction):
            if (j == 3) and (len(prediction) != i+1):
                conditional_probability.append(prediction[i+1])
                print i+1, len(prediction), j, conditional_probability
        next_choice_prob = pd.DataFrame(conditional_probability, columns=['selection'])
        return next_choice_prob.groupby('selection').size().div(len(next_choice_prob)).idxmax()
