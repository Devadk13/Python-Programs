print("Program to check whether the number is an Armstrong number number")
import math

def isArmstrong(n,length):

	d=n
	sum=0
	i=2
	while(n>0):
		r=n%10
		sum=sum+(r**length)
		n=n//10
	return (True if sum==d else False)

n=input("Enter the number ")
length=len(n)

n=int(n)

print(isArmstrong(n,length))





