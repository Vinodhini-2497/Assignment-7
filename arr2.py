import logging as lg
import array
lg.basicConfig(filename='arr2.log',level= lg.INFO,format='%(asctime)s - %(message)s') 
a=[2,45,67,3]
large=a[0]
for i in range(1,len(a)):
    if a[i]>large:
        large=a[i]
print("Largest number in array is:",large)