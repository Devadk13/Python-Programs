print("Python Program to replace all 0's with 5")


def replace(n):
	num=0
	while(n>0):
		r = n % 10
		if(r==0):
			r = 5
		num=num*10 +r
		n=n//10

	sum=0
	while(num>0):
		r=num%10
		sum=(sum*10)+r
		num=num//10

	return sum
n=int(input("Enter the number "))
print(replace(n))
