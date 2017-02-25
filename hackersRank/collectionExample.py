# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict, Counter

#n = input()
#print n
#print raw_input().split()
'''
n=raw_input()
print n
sizes_agg = Counter(map(int, raw_input().split()))

print "sizes_agg",sizes_agg
customers = []
for i in xrange(input()):
    customers.append(map(int, raw_input().split()))

print customers
d = defaultdict(list)
for size, cost in customers:
    d[size].extend([cost])
print d
total = 0
for i, k in sizes_agg.items():
    print i
    print d[i][:k]
    total += sum(d[i][:k])
print total
'''
from collections import defaultdict, Counter
no_shoes=input()
print no_shoes
shoes_sizes=Counter(map(int,raw_input().split()))
print "sizes",shoes_sizes
no_customers=input()
print "customers",no_customers
customerlist=list()
for i in xrange(no_customers):
    customerlist.append(map(int,raw_input().split()))
print customerlist
d=defaultdict(list)
for item,size in customerlist:
    d[item].extend([size])
print d.items()

print shoes_sizes.items()
total=0
for i,k in shoes_sizes.items():
    total+=sum(d[i][:k])
print total