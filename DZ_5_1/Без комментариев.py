program_lines = []
line = input()
while line != "":
    program_lines.append(line)
    line = input()

for line in program_lines:
    i = 0
    while i < len(line):
        if line[i] == "#":
            break
        i += 1
    line_without_comment = line[:i].strip()
    if line_without_comment != "":
        print(line_without_comment)