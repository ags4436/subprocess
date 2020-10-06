from subprocess import Popen,STDOUT,PIPE
while True:
        query = input('$ ')
        query = query + '\n'
        p = Popen(['bc','-q','-i'], stdout=PIPE, stdin=PIPE, stderr=STDOUT, shell=True)
        result = p.communicate(query.encode(), timeout=1)
        print(result[0].decode().rstrip())
