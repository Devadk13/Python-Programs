print("Climbing stairs Problem")

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)

def count(s):
    return fib(s+1)

print("Enter the number of steps")
s=int(input())
ways=count(s)
print(ways)
