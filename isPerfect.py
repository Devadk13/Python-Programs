print("Program to check whether the number is a perfect number")
import math

def isPerfect(n):


	sum=1
	i=2
	while(i*i<=n):
		if(n%i==0):
			sum=sum+i+(n/i)

		i=i+1

	return sum

n=int(input("Enter the number "))
if isPerfect(n)==n:
	print("Perfect Number")

else:
	print("Not Perfect Number")

