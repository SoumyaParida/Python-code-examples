from collections import OrderedDict

n=input()

mydict=OrderedDict()

for i in xrange(n):
    name, price = raw_input().rsplit(' ', 1)
    if name in mydict:
        mydict[name] += int(price)
    else:
        mydict[name] = int(price)

print mydict.items()
for name,price in mydict.items():
    print name,price