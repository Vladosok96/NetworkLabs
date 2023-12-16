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
        if line[0] != ' ':
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
        for _ in range(3):
            self.popen.stdout.readline()
        for i in range(len(self.ip_list)):
            line = self.popen.stdout.readline()
            self.stat_list.append([line[:3], line[4:10], line[11:27], line[28:44], line[45:-2]])
            self.popen.stdout.readline()
        return self.stat_list
