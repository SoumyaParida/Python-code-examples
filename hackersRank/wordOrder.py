from collections import Counter, OrderedDict

n=input()
count=0
value=OrderedDict()
for i in xrange(n):
    item=raw_input()
    if item in value:
        value[item]+=1
    else:
        value[item]=1

print len(value)
values1=value.values()
print ' '.join((str(x) for x in values1))
