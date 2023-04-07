stack = input().split()
current = []
i = 0
sign = ''

while len(stack) != 1:
    if stack[i + 1].isdigit() is not True:
        i += 1
        sign = stack[i]
        del stack[i]
        i -= 1

        if sign == '@':
            buff = stack[i]
            stack[i] = stack[i - 2]
            stack[i - 2] = stack[i - 1]
            stack[i - 1] = buff

        else:
            current.append(stack[i])

            if sign == '~':
                stack[i] = - int(current[0])
            elif sign == '!':
                stack[i] = 1
                for j in range(1, int(current[0]) + 1):
                    stack[i] = stack[i] * j
            elif sign == '#':
                stack.insert(i, stack[i])
                i += 1
            else:
                del stack[i]
                i -= 1
                current.append(stack[i])
                if sign == '+':
                    stack[i] = int(current[1]) + int(current[0])
                elif sign == '-':
                    stack[i] = int(current[1]) - int(current[0])
                elif sign == '*':
                    stack[i] = int(current[1]) * int(current[0])
                elif sign == '/':
                    stack[i] = int(current[1]) // int(current[0])

        current = []

    else:
        i += 1

print(stack[0])
