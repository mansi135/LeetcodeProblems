def mergesort(l):
    if len(l)==1:
        return l
    else:
        l1=l[:int(len(l)/2)]
        l2=l[int(len(l)/2):]
        l1=mergesort(l1)
        l2=mergesort(l2)
        return merge(l1,l2)


def merge(l1,l2):
    l3=[]
    i1=0
    i2=0
    while i1<len(l1) and i2<len(l2):
        if l1[i1]<l2[i2]:
            l3.append(l1[i1])
            i1+=1
        else:
            l3.append(l2[i2])
            i2+=1
    while i1<len(l1):
        l3.append(l1[i1])
        i1+=1
    while i2<len(l2):
        l3.append(l2[i2])
        i2 += 1

    return l3






l=[1,0,88,-1,7]
l=[1,0]
print(mergesort(l))
