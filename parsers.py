import subprocess


class PathPingParser:

    def __init__(self, address):

        self.ip_list = []
        self.stat_list = []

        self.popen = subprocess.Popen(f"pathping {address}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                      text=True, encoding='cp866')
        for _ in range(3):
            self.popen.stdout.readline()

    def get_next_ip(self):
        line = self.popen.stdout.readline()
        if len(line) < 3 or not line[2].isdigit():
            return False
        line = line[5:]
        if '[' not in line:
            result = line[:-2]
            self.ip_list.append(result)
            return result
        else:
            try:
                result = line.split('[')[1].split(']')[0]
                self.ip_list.append(result)
                return result
            except:
                pass

    def get_stat(self):
        line = self.popen.stdout.readline()
        while not line[2].isdigit():
            line = self.popen.stdout.readline()
        for i in range(len(self.ip_list)):
            if not line[2].isdigit():
                break
            self.stat_list.append([line[:3], line[4:10], line[11:27], line[28:44], line[45:-2]])
            self.popen.stdout.readline()
            line = self.popen.stdout.readline()
        return self.stat_list


class IpconfigParser:
    def __init__(self):
        self.popen = subprocess.Popen(f"ipconfig /all", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                      text=True, encoding='cp866')
        self.adapters = []

        for _ in range(9):
            self.popen.stdout.readline()

        state = 0
        title = ''
        parameters = ''
        line = self.popen.stdout.readline()
        while line != '':
            if state == 0:
                title = line[:-2]
                parameters = ''
                state = 1
                self.popen.stdout.readline()
            elif state == 1:
                if line == '\n':
                    state = 0
                    self.adapters.append([title, parameters])
                parameters += line
            line = self.popen.stdout.readline()


class PingParser:
    def __init__(self, address):
        self.popen = subprocess.Popen(f"ping {address}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                      text=True, encoding='cp866')

        self.is_done = False
        self.info = ''

    def read(self):
        line = self.popen.stdout.readline()
        if line == '':
            self.is_done = True
            return
        self.info += line
