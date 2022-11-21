import time


start_time = time.localtime()
print(f"TImer started at {time.strftime('%X', start_time)}")

# Wait for User to stop Timer
input("Press any key to stop timer ")

stop_time = time.localtime()
print(time.mktime(start_time))
print(time.mktime(stop_time))
difference = time.mktime(stop_time) - time.mktime(start_time)
print(f"Timer stopped at {time.strftime('%X', stop_time)}")
print(f"Total Time: {difference} Seconds")
print(f"Total time in other format : {difference//60} minutes")
#print(f"Total time in other format : {time.('%s', difference)} minutes")