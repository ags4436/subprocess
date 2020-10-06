# Program to access bh from python using subprocess and execute the calculator
# Since this create different Pids for we cannot assign vaiables as we do in bh, for that we need to do multi threading 
from subprocess import Popen,STDOUT,PIPE
while True:
        query = input('$ ')
        query = query + '\n'
        p = Popen(['bc','-q','-i'], stdout=PIPE, stdin=PIPE, stderr=STDOUT, shell=True)
        result = p.communicate(query.encode(), timeout=1)
        print(result[0].decode().rstrip())

