def linearSearch(myItem,num,myList):
    counter=0
    for item in myList:
        if num <=counter:
            if item==myItem:
                return counter
            else:
                counter=counter+1
        else:
            return None
sentinel=''
input='\n'.join(iter(raw_input, sentinel))
print input
myitem,num, value=input.split('\n')
print linearSearch(myitem,num,value)
