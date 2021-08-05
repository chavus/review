
my_list = [0, 1, 2, 3]
len(my_list)
my_list[0] # 0
my_list[-1] # 3
my_list[1:3] #slice -> 1,2
# my_list[0] = "zero" # list assignment, mutable objects
my_list.append(4)
my_list.extend([5, 6])

for i in my_list:
    print(i)

print([i**2 for i in my_list if i%2==0])

my_dict = {"name": "chava",
           "age": 34,
           "lucky_nums": [17, 21]
           }

my_tuple = ("red","blue")
my_set = {1,2,2,3,4}


