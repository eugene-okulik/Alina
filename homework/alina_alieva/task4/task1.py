my_dict = {'tuple': (1, 2, 3, 4, 5), 'list': ['one', True, 1.5, 2, 'name'], 'dict': {1: 'lal', 2: False, 3: 1.4,
                                                                                     4: 'trylal', 'one': 1},
           'set': {100, 200, 300, 400, 'string'}}

print((my_dict['tuple'])[-1])
my_list = my_dict['list']
my_list.append(123)
deleted = my_list.pop(1)
print(my_list)

my_dict2 = my_dict['dict']
my_dict2[('i am a tuple',)] = 1, 'Adbnnfmf', 4, 8
print(my_dict2)
deleted_item = my_dict2.pop(1)
print(my_dict2)

my_set = my_dict['set']
my_set.add('added element')
print(my_set)
my_set.remove(400)
print(my_set)
print('The DICTIONARY:', (my_dict))
