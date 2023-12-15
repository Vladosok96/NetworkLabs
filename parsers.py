import subprocess
import re


class PathPingParser:

    def __init__(self, address):

        self.list = []

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
            self.list.append(result)
            return result
        else:
            try:
                result = line.split('[')[1].split(']')[0]
                self.list.append(result)
                return result
            except:
                pass

    def get_stat(self):
        for _ in range(3):
            self.popen.stdout.readline()
        for i in range(len(self.list)):
            print(re.split(' {5}| {4}| {3}| {2}| |/|=', self.popen.stdout.readline()))
            self.popen.stdout.readline()