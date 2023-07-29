
import math
print("Program to check whether the number is a valid perfect square or not")


n=int(input("Enter the number"))


def isSquare(n):
	if(n>=0):
		s=int(math.sqrt(n))


		if ((s*s)==n):
			return True
		else:
			return False
	return False

if (isSquare(n)==True):
	print(f"{n} is valid perfect square")
else:
	print(f"{n} is not a valid perfect square")



