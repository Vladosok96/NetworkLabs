def parse_pathping(popen):
    IPs = []
    state = 0
    counter = 0
    while True:
        line = popen.stdout.readline()
        if len(line) == 0:
            break
        if counter > 2 and state == 0:
            if line[0] != ' ':
                state = 1
                return IPs
            line = line[5:]
            if line[0].isdigit():
                IPs.append(line[:-2])
            else:
                try:
                    IPs.append(line.split('[')[1].split(']')[0])
                except:
                    pass
        counter += 1

    return IPs
