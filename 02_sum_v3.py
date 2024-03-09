#
# A Program to add 2 numbers in Python
# Author: Pavan.  06th Mar, 2024
#
import sys
print(f"the programme name is : {sys.argv[0]}")
if(len(sys.argv) == 3):
	num1=int(sys.argv[1])	
	num2=int(sys.argv[2])
else:
	print("ERROR:please pass 2 numbers as arguments to programme")
	exit(0)
sum=num1+num2
print(f"sum={sum}")