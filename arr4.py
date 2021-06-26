#Program to Split the array and add the first part to the end
import array
import logging as l
l.basicConfig(filename='arr4.log', level=l.INFO, format='%(asctime)s-%(message)s')
a=[1,2,3,4,5]
a1=[]
shift=2
print("The original array",a) 

for i in range(0,shift):
    while(a[i]<=2):
        temp=a[i]
        a1.append(temp)
        a.remove(a[i])
        print("The spilt array of 2 indexes ", a1)
print("The original array after the spilt",a) 

try:
    sumofarray=[]
    sumofarray=a+a1
    print("The sum of array is:",sumofarray)
    
except Exception as  e:
    l.ERROR(e)




       
      