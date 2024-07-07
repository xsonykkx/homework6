my_dict = {'Sonya' : 2002 , 'Vanessa' : 1990, 'Farhan' : 2006}
print(my_dict)
print(my_dict [ 'Sonya'])
print(my_dict.get('Oksana'))
my_dict [ 'Maya' ] = 1997
print(my_dict ['Maya'])
my_dict.update({'Shura' : 2000,
                'Masha' : 2001})
a = my_dict.pop('Vanessa')
print(a)
print(my_dict)

my_set = { 52, 'Liuba', 1.1, 52, 'Maya', 'Maya'}
print(my_set)
my_set.add(10)
my_set.add('yabloko')
my_set.remove(1.1)
print(my_set)
