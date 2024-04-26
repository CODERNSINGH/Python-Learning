# We have to make a programme who whis us according to time 

import time 
timestrf = time.strftime('%H:%M:%S') 


print("Current Time is: ",timestrf)
if (timestrf <= '10:00:00'):
    print("Good Morning")
elif(timestrf >= '10:00:00' and timestrf <= '21:00:00'):
    print("Good Evening")
else:
    print("Good Night")