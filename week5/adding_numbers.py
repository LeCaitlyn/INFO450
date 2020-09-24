import sys

def add_them_all(filename):
    sum = 0

    with open(filename, 'r') as f:
        contents = f.read()
    number_list = contents.split()

    for i in range(0, len(number_list)): 
        number_list[i] = int(number_list[i])
        sum = sum + number_list[i]

    return sum

if __name__ == "__main__":
    fname = sys.argv[1]
    print(f"Processing {fname}")
    print(add_them_all(fname))