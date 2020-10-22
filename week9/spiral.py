# import numpy as np # I also commented this out since it would interfere with my VS Code and only worked in Jupiter Notebook
 
############################## Plans To Create Spiral ##############################

# My initial thoughts are that we need to start with an empty matrix. We need to create a matrix of size width*height (501*501 in this case) with values of "None"
# Once we do this, we can find the center of the matrix and place a 1 in this "location"
# In order to create our spiral, we need to start by placing a 2 in the spot to the right. We can set up "directions" to move between each of the "dimensions of arrays" 
# We can assign directions to move around the matrix. For example, if we want to move "right" we would add one to our column and 0 to our row (1,0)
# We can create the 4 "directions" by doing this for up, down, left, and right. [up = (0,-1), down = (0,1), right = (1,0), and left = (-1,0)]
# The spiral is created by "turning right" if you will, when there is a "None" value after "turning right" 
# To get from the 2 spot to the spot where 3 needs to be (one row down) we are "turning right" 
# We will need to "turn right" again to get to 4 and this requires changing our direction to "left." 
# However, to get to 5, we do not want to change direction. We can put this into our function easily because we will want to keep the same direction when we cannot "turn right" 
# We will keep following this pattern until the spiral is complete
# Each time we see if we need to turn right or not, we add one to a counter first to make sure our spiral follows integers in the order of 1, 2, 3, ...

############################## Plans To Sum Diagonals ##############################

# After we have our spiral matrix, we need to sum up the diagonals. This can easily be put inside the function that actually creates the matrix
# We initialize our diagonal sum values to 0. We also want to find the center of the matrix here, which we know will be 1 since we do not want to double count it
# We will subtract the "center" at the end
# We can find the top left to bottom right diagonal easily since the indecies will always match (i = i)
# For the opposite diagonal, we can grab the row index and kind of mirror it by taking the total length minus the index minus 1
# Then we sum these two diagonals together and subtract 1 (the center) to get the total sum
# I used numpy to take a look at the matrix visually while I was solving the problem to make sure it looked right
# However, I commented it out for the sake of only returning the sum

############################### My Code With Comments ###############################

up, down, left, right = (0, -1), (0, 1), (-1, 0), (1, 0)    # Create directions for the spiral
turn_right = {up: right, right: down, down: left, left: up} # where the location "moves" to when we "turn right." If we initialize at up, our first turn will be to the right

def spiral_cw(width, height):
    if width  < 1 or height < 1: 
        raise ValueError                                 # If our matrix n*m is too small, we will quit and output an error
    x, y = width // 2, height // 2                       # Find the center of the spiral without float values (gets the indicies for the center)
    direction_x, direction_y = up                        # Initialize our direction at "up" so our first turn will be "right"
    matrix = [[None] * width for _ in range(height)]     # Create a matrix of n*m with "None" values
    count = 0                                            # Start our count at 0 so our center values becomes 1 when we start
    while True:                                          # The beginning of our spiral function
        count += 1                                       # Add 1 each time we place a new value in a new location regarless of turning
        matrix[y][x] = count                             # Put whatever iteration of the function we are on in the location we are at
        new_direction_x, new_direction_y = turn_right[direction_x, direction_y]            # Setting our new direction since we initialized at up
        new_x, new_y = x + new_direction_x, y + new_direction_y                            # This is our new location after turning right
        if (0 <= new_x < width and 0 <= new_y < height and matrix[new_y][new_x] is None):  # If the new location is in the correct range and the cell in the matrix is empty after turning right, then turn right
            x, y = new_x, new_y                                             # This sets the location for the new x and y after verifying that we are not done with the matrix and we can turn right
            direction_x, direction_y = new_direction_x, new_direction_y     # This sets the direction for the time being until we can turn right again      
        else:
            x, y = x + direction_x, y + direction_y           # If we cannot turn right, AND we are still within the limits of the matrix, 
            if not (0 <= x < width and 0 <= y < height):      # then we get the new count value and keep the same direction
                length = len(matrix)                          # The while loop ends here when our x and y are greater than width*height
                diagonal_1 = 0                                # We initialize our sum of diagonal values to 0
                diagonal_2 = 0
                center = matrix[width // 2][height // 2]      # We set the center of the matrix here (in case it isn't 1 for some reason)
                for i in range(length):                       # We iterate through each of the values in the matrix
                    diagonal_1 += matrix[i][length - i - 1]   # For the values of the matrix where the i is equal to the total length - i - 1, we add those values to the sum
                    diagonal_2 += matrix[i][i]                # We also add any values where i = i
                return (diagonal_1 + diagonal_2 - center), matrix           # We return the sum of both diagonals while subtracting the center. We also return the matrix for visual purposes
            
print(spiral_cw(501,501)[0])        # We can get the sum by taking the 0th index of the spiral_cw function

# np.array(spiral_cw(501,501)[1])   # We can use numpy to get the array of the matrix "shaped" by taking the 1st index of the spiral_cw function
