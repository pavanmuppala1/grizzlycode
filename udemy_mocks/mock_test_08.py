def check(x):
    if (x[0] == x[-1]):
       return True
    else:
       return False

print(check([10, 20, 30, 40, 10]))
print(check([40, 20, 30, 40, 10]))