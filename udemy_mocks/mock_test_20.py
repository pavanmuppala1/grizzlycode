dict1 = {'one': 1, 'two': 2, 'three':3}
dict2 = {'one': 1, 'two': 5, 'four': 8}
dict3 = dict(dict1)
dict4 = dict(dict2)
dict3.update(dict2)
dict4.update(dict1)
print(dict3 == dict4)