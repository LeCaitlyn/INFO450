
# Page 84 Assignment

killed_color = 'green'

def get_points(killed_color):
    earned_points = 0

    if killed_color == 'green':
        earned_points = 5
    elif killed_color == 'yellow':
        earned_points = 10
    elif killed_color == 'red':
        earned_points = 15
    elif killed_color == 'blue':
        earned_points = 3
    return earned_points

if __name__ == "__main__":
    pts = get_points('red')
    print(f"For {killed_color}, you got {pts} points.")

# If I wanted to check to see if your function is correct (or if something is missing)
    assert get_points('red') == 15
    assert get_points('yellow') == 10
    assert get_points('green') == 5
    assert get_points('blue') == 3



