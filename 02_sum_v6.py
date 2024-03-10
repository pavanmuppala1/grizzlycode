#
# A Program to add 2 numbers in Python
# Author: Pavan.  06th Mar, 2024
#
import sys
sum=0
for number in sys.argv[1:]:
	sum = sum+float(number)
print(f"sum of numbers - {str(sys.argv[1:])} = {sum}")