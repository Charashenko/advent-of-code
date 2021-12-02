with open('values', 'r') as f:
    # Two parts combined
    dep = 0
    hor = 0
    aim = 0
    lines = f.readlines()
    for line in lines:
        line = line.split(" ")
        if line[0] == 'forward':
            hor += int(line[1])
            dep += aim*int(line[1])
        elif line[0] == 'up':
            aim -= int(line[1])
        elif line[0] == 'down':
            aim += int(line[1])
    print(dep*hor)