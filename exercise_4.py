

my_list = [9, 5, 6, 8, 4]
my_list.sort()
print(my_list)
highest = 0
runnerup = 0
temp = 0
for i in my_list:
    if i > highest:
        highest = i
    elif i <= highest and i > runnerup:
        runnerup = i
"""
for i in my_list:
    if i > runnerup and i != highest:
        runnerup = i
"""
print("highest: " + str(highest))
print("runnerup: " + str(runnerup))