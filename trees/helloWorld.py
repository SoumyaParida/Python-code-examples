def solution(n):
    d=[0]*30
    l=0
    while (n>0):
        d[l]=n%2
        n//=2
        l+=1
    print d

    for p in xrange(1,1+l):
        print xrange(1, l)
        ok=True
        print xrange(l-p)
        for i in xrange(l-p):
            if d[i]!=d[i+p]:
                ok=False
                break
        if p !=l and ok:
            return p
    return -1

print solution(955)