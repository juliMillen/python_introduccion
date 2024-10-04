## List Comprehension ##

my_original_list = [35, 24, 62, 30, 24, 16]

my_list = [i for i in my_original_list]
print(my_list) ##se transforma una lista en otra lista


my_range = range(8)
print(list(my_range))

my_list = [i + 1 for i in range(8)]
print(my_list)


my_list = [i * 2 for i in range(8)]
print(my_list)


my_list = [i * i for i in range(8)]
print(my_list)