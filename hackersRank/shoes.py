from collections import Counter,defaultdict
mn=map(int,raw_input().split())
print mn
values=defaultdict(list)
count=1
for i in xrange(mn[0]):
    values[raw_input()].extend([count])
    count=count+1
print values.items()

for j in xrange(mn[1]):
    item=raw_input()
    if values.has_key(item):
        print ' '.join(map(str,values[item]))
    else:
        print -1