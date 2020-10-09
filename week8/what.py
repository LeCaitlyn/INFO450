import logging
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

def find_runner_up(score_list=None):
    last_list = []  
    score = []

    if len(score_list) > 2:
        new_list = score_list.sort()
        new_list_2 = score_list.sort()
        for x in new_list:
            if x not in new_list_2:
                last_list.append(x)
        return last_list

    elif len(score_list) < 1:
        print("There is no runner up.") 
         
    else:
        print("There is a tie!")
        
    last_list = last_list.sort()
    score = last_list[-2]

    return(score)
            

if __name__ == "__main__":
    find_runner_up(score_list=[1, 2, 3, 4, 5, 5, 5, 5, 5])