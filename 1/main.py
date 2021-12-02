with open('values', 'r') as f:
    # Common variable
    lines = f.readlines()

    # First part 
    prev_value = 0
    n_increased = 0
    for line in lines:
        if prev_value < int(line):
            n_increased += 1
        prev_value = int(line)
    print(n_increased-1)

    # Second part
    prev_sum = 0
    cur_sum = 0
    n_increased = 0
    for i in range(len(lines)):
        cur_sum += int(lines[i])
        if i + 1 < len(lines):
            cur_sum += int(lines[i + 1])
        if i + 2 < len(lines):
            cur_sum += int(lines[i + 2])
        if cur_sum > prev_sum:
            n_increased += 1
        prev_sum = cur_sum
        cur_sum = 0
    print(n_increased-1)
