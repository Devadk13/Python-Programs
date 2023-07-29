# Conversion table of remainders to
# hexadecimal equivalent
conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
					5: '5', 6: '6', 7: '7',
					8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
					13: 'D', 14: 'E', 15: 'F'}


def convertHex(n):
	h=''
	while(n>0):
		r=n%16
		h=conversion_table[r]+h
		n=n//16

	return h

n=int(input("Enter the number"))
print(convertHex(n))
