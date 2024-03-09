tup_a = (0,1,2)
tup_b = (2,3,4)
list_c = []
for el in tup_a:
        if el not in tup_b:
                list_c.append(el)
print(list_c)