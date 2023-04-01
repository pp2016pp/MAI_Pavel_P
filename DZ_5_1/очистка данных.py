while True:
    try:
        line = input().strip()
        if not line:
            break
        if line.startswith('##'):
            line = line[2:]
        if line.endswith('@@@'):
            continue
        print(line)
    except EOFError:
        break