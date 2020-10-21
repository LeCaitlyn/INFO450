
up, down, left, right = (0, -1), (0, 1), (-1, 0), (1, 0) # directions
turn_right = {up: right, right: down, down: left, left: up} # old -> new direction

# Find the center of the spiral
def spiral_cw(width, height):
    if width  < 1 or height < 1:
        raise ValueError
    x, y = width // 2, height // 2
    direction_x, direction_y = up
    matrix = [[None] * width for _ in range(height)]
    count = 0
    while True:
        count += 1
        matrix[y][x] = count
        new_direction_x, new_direction_y = turn_right[direction_x, direction_y]
        new_x, new_y = x + new_direction_x, y + new_direction_y
        if (0 <= new_x < width and 0 <= new_y < height and matrix[new_y][new_x] is None):
            x, y = new_x, new_y
            direction_x, direction_y = new_direction_x, new_direction_y
        else:
            x, y = x + direction_x, y + direction_y
            if not (0 <= x < width and 0 <= y < height):
                return matrix

def print_matrix(matrix):
    width = len(str(max(el for row in matrix for el in row if el is not None)))
    fmt = "{:0%dd}" % width
    for row in matrix:
        print(" ".join("_"*width if el is None else fmt.format(el) for el in row))

print_matrix(spiral_cw(15, 15))



find_sum(spiral_cw(15,15))
# Make a clockwise spiral starting from the center of a matrix
    
# Find each of the values on the diagonal (if n = m)

# Add up each of the diagonals

# Return the sum

