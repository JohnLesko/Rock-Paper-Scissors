from interface import Interface


def r_p_s():
    """
    rock = 1
    paper = 2
    scissors = 3
    """
    probability_list = []
    while user_prediction != 'stop':
        user_prediction = raw_input('Input rock, paper, scissors: ').lower()
        probability_list.append(user_prediction)
        print probability_list


if __name__ == '__main__':
    Interface
