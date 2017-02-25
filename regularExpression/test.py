import re
print bool(re.search(r"ly","similarly"))
print bool(re.match(r"ly","similarly"))
print bool(re.match(r"ly","ly should be in the beginning"))
print re.split("-","+91-011-2711-1111")
