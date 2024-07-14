# Словари и множества
my_dict = {'Anton': 1980, 'Alla': 1981, 'Arseny': 2006, 'Ilya': 2007}
print(my_dict)
print(my_dict['Alla'])
print(my_dict.get('Max'))
my_dict['Olya'] = 1961
print(my_dict)
my_dict['Igor'] = 1957
print(my_dict)
my_dict.update({'Serg': 1983, 'Makar': 2011, 'Ylya': 2008})
del my_dict['Igor']
print(my_dict)
my_dict.pop('Makar', 'Serg')
print(my_dict)

my_set = {1, 2, 3, 4, 12, 13, 'Alla', 14, 2, 3, 4, True, (123, 2, 3)}
print(my_set)
print(set(my_set))
my_set.add(99)
my_set.add(88)
print(my_set)
my_set.remove('Alla')
print(my_set)