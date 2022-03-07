from sys import argv
from itertools import count
name = argv[0]
start = int(argv[1])
end = int(argv[2])
for i in count(start):
    if i > end:
        break
    else:
        print(i)