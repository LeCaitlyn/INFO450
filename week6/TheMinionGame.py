def give_points(substring):
    stuart_points = 0
    kevin_points = 0
    vowels = ['a', 'e', 'i', 'o', 'u']

    if substring.lower[0] in vowels:
        kevin_points += 1

    else:
        stuart_points += 1

    return stuart_points, kevin_points


def minion_game(string):
    # your code goes here
    stuart_score = 0
    kevin_score = 0
    string
    first_two = string[0:2]
    for position in range(len(string)):
        for length in range(len(string) - position):
            substring = string[position:position+length + 1]
            temp_stuart_points, temp_kevin_points = give_points(substring)
            stuart_score += temp_stuart_points
            kevin_score += temp_kevin_points

    if stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    elif kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")



if __name__ == '__main__':
    give_points("BANANA")