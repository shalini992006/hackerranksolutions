import re
n = int(input())
for _ in range(n):
    line = input()
    if line.lstrip().startswith('#'):
        print(line)
    else:
        line = re.sub(r'(?<=)&&(?=)', 'and', line)
        line = re.sub(r'(?<=)\|\|(?=)', 'or', line)
        print(line)
   