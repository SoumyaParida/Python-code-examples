from collections import deque
d=deque()
n=input()
for i in xrange(n):
    item=raw_input().split()
    if len(item)>1:
        getattr(d, item[0])(int(item[1]))
    else:
        getattr(d, item[0])()
print ' '.join(str(x) for x in d )