def myfunc(message,count):
    myfile = open('my_messages3.txt', 'w')
    myfile.truncate(0)
    for i in range(0,count):
        #print(message)
        myfile.write(message+'\n')
    myfile.seek(0)
    myfile.close()
    myfile2 = open('my_messages3.txt','r+')
    print(myfile2.read())
    myfile.close()

while True:
    mymessage = input('Enter your message')
    mycount = input('How many times to print?')
    if not mymessage:
        continue
    myfunc(mymessage, int(mycount) if mycount else 1)
    break
