#
# A Program to add 2 numbers in Python
# Author: Pavan.  06th Mar, 2024
#
import sys
print(f"the programme name is : {sys.argv[0]}")
if(len(sys.argv) == 6):
	num1=int(sys.argv[1])	
	num2=int(sys.argv[2])
	num3=int(sys.argv[3])
	num4=int(sys.argv[4])
	num5=int(sys.argv[5])

else:
	print("ERROR:please pass 5 numbers as arguments to programme")
	exit(0)
sum=num1+num2+num3+num4+num5
print(f"sum of 4 numbers {num1} + {num2} + {num3} + {num4} + {num5} = {sum}")