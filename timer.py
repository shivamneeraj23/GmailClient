import time
import os
import Gmail_SentMail

#Getting the Current Time of the System
current_time=time.localtime(time.time())

#Getting the User Input Time
while True: #Infinite loop
    time_input = raw_input("Please enter the time in HH:MM:SS format: ")
    try:
        user_time = time.strftime("%Y %m %d")
        my_time = time.strptime("%s %s" % (user_time, time_input),
                             "%Y %m %d  %H:%M:%S")
        break #this will stop the loop
    except ValueError:
        print "The time you entered is incorrect. Try again."

#time_differnce
def difference_of_time(t1,t2):
    t1_hour,t1_min,t1_sec=current_time.tm_hour, current_time.tm_min, current_time.tm_sec
    t2_hour,t2_min,t2_sec=my_time.tm_hour, my_time.tm_min, my_time.tm_sec
    t1=(t1_hour*60*60)+(t1_min*60)+t1_sec
    t2=(t2_hour*60*60)+(t2_min*60)+t2_sec
    return (t2-t1)


time.sleep(difference_of_time(my_time,current_time))
Gmail_SentMail.main()
#execfile(Gmail_SentMail.py)
