
tmpList = []
secList = []
print("please enter a sentence ")
my_str = input()
tmpList.extend(my_str)

for i in my_str:
    temp = int(ord(i))
    if temp >= 65 and temp <= 90:
        temp = i.lower()
        secList.append(temp)
    elif temp >= 97 and temp <= 122:
        temp = i.upper()
        secList.append(temp)
    elif temp == 32:
        secList.append(' ')
    else:
        secList.append(temp)
print(''.join(secList))