import re
def substring(str):
    valid = re.match('^[\w-]+$', str) is not None
    length = len(str)
    values = set()
    flag=0
    pos = list()
    if valid:
        print range(length)
        for i in range(length):
            s = str[i: i + length]
            print s
            if any(x.isdigit() for x in s):
                continue
            else:
                if any(y.isupper() for y in s):
                    values.add(s)

        for item in values:
            pos.append(str.find(item))
        if pos:
            if max(pos) >=1 and max(pos) <=200:
                return max(pos)
            else:
                return -1
        else:
            return -1
    else:
        return -1

str="a0Ba"
print substring(str)

