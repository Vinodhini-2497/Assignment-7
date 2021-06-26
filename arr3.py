import array
import logging as l
l.basicConfig(filename='arr3.log', level=l.INFO, format='%(asctime)s-%(message)s')
al=[1,2,3,4,5]
ar=[1,2,3,4,5]
j=2#shift 2 in left
k=2#shift 2 in right
print("before the iteration for left array",al)
print("before the iteration for left array",ar)
def leftrotatearray(al,j):
    for l in range(0,j):
        temp=al[0]
        for i in range(0,(len(al)-1)):
            al[i]=al[i+1]
        al[len(al)-1]=temp
    return(al)

def rightrotatearray(ar,k):
    for m in range(0,k):
        temp=ar[len(ar)-1]
        for d in range(len(ar)-1,0,-1):
            ar[d]=ar[d-1]
        ar[0]=temp
    return(ar)
    
#leftarray=leftrotatearray(a,j)
#rightarray=rightrotatearray(a,k)
print("after left rotation array is:", leftrotatearray(al,j))
print("after right rotation array is:",rightrotatearray(ar,k))