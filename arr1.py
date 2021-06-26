import logging as lg
import array
lg.basicConfig(filename='arr1.log',level= lg.INFO, format='%(asctime)s - %(message)s')   
try:
    ar=[]
    sum=0
    n=int(input("Enter the value of user input  index array:")) 
    for i in range(0,n):
        value=int(input("please enter the index of list value %d:"%i))
        ar.append(value)
        sum=sum+value
        print("sum of array is ", sum)
except IndexError as a:
        lg.ERROR(a)
      
    