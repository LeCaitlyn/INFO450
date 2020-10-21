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
    points = find_runner_up([1, 3, 2, 600, 4])
    logging.debug(points)
    