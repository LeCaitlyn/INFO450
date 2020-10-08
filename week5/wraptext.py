import textwrap

def wrap(string, max_width):
    x = 0
    for letter in string:
        print(letter)
        x += 1
        if x == max_width:
            print("".join(temp.string))
            temp.string = ""
            x = 0
    print("".join(temp.string)
    return ""

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)



