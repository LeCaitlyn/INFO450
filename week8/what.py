import logging
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

def find_runner_up(score_list):
    score = []
    score_list = list(set(score_list))

    if not score_list or score_list == []:
        print("There is no runner up.") 

    elif len(score_list) == 1:
        print("There is a tie!")

    elif len(score_list) >= 2:
        new_list = sorted(score_list)
        score = new_list[-2]
        
    return(score)

if __name__ == "__main__":
    points = find_runner_up([5, 3, 4, 7, 8, 4, 1, 8, 8, 6, 7])
    logging.debug(points)