# Files
# Json
# Csv
# Hackerrank

# Function open allows you to open a file path
# First two parameters are the file name/path and then the mode (tells you what you will be doing with the file)

# Always close the files after you open them!!!
# This can be done with the .close() function

# KEYWORD "with" sets up a block of code that closes automatically after the next indented line is completed

# Cat is a command to print out a file

# Split function -> split this line of string on this character, we will get an array of the things that are 
# between the character we split on

# If we want to make something json, use "import json" then use the json.dumps() function 
# Json.dumps() has some optional parameters, sort_keys, indent, etc

# CSV
# "import csv" package

# Python does not differentiate between a string and a character

with open("iliad.txt", 'r') as iliad, open("bigwords.txt", "w") as big_words, open("smallwords.txt", "w") as small_words:
    contents = iliad.read()
    for char in '?!-=+/\'"-.,\n':
        contents = contents.replace(char,' ') # replace those characters with whitespace
    contents = contents.lower() # make everything lowercase
    word_list = contents.split()
    print(word_list[0:100]) # print out the first 100 words
    for word in word_list:
        if len(word) > 5:
            big_words.write(f"{word}\n") #\n means the new line
        else:
            small_words.write(f"{word}\n")


# Slide 17 - the length of the list mapped is the same length as the list word_list















