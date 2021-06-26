#Program to check if given array is Monotonic

import array
import logging as l
l.basicConfig(filename='arr5.log', level=l.INFO, format='%(asctime)s-%(message)s')
def monoarr(a):
    try:
        for i in range(len(a)-1):
            if a[i]<=a[i+1]:
                return ("The given array is monotonic increasing",a)
            else:
                if a[i]>=a[i+1]:
                    return ("The given array is monnotonic decreasing",a)
    except Exception as e:
        return l.ERROR(e)  
    
    
a=[1,2,3,4,5]
b=[5,4,3,2,1]

print(monoarr(a))
print(monoarr(b))