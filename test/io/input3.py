"""
read input from a file, like input2
get multiple lines
"""

with open("./file/input3.txt", 'r') as f:
    for line in f:
        # there is a '\n' at the end of the 'line'
        print(line)
        print(line.strip())