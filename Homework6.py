my_dict = {'Иванов': 1980, 'Петров': 1990, 'Сидоров': 2000}
print(my_dict)
print(my_dict['Иванов'])
print(my_dict.get('Кикабидзе'))
my_dict.update({'Кузнецов': 1960, 'Пастухов': 1950})
a = my_dict.pop('Кузнецов')
print(a)
print(my_dict)

my_set = {10, 20, 10, 20, 'Вася', 'Петя', 'Вася', 'Петя', (1, 2 ,3)}
print(my_set)
my_set.add(50)
my_set.add('Маша')
my_set.remove('Петя')
print(my_set)
