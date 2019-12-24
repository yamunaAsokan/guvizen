newlist=list(input('enter the new list'))
def swaplist(newlist):
    newlist[0],newlist[-1]=newlist[-1],newlist[0]
    return(newlist)
print(swaplist(newlist))
