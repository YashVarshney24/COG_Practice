

import math as mt
n = int(input("Enter a number"))
print(n)

def Table(n):

	if (n <= 0):
		return

	arr = list()
	arr.append("0")
	arr.append("1")

	i = 2
	j = 0
	while(True):

		if i >= 1 << n:
			break
      	
		for j in range(i - 1, -1, -1):
			arr.append(arr[j])
	
		for j in range(i):
			arr[j] = "0" + arr[j]

		for j in range(i, 2 * i):
			arr[j] = "1" + arr[j]
		i = i << 1

	# print contents of arr[]
	for i in range(len(arr)):
		print(arr[i])

Table(n)