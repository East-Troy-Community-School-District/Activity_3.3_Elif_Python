'''
Reflex
Pawelski
1/27/2025

Instructions:
1.  Before you run the program, predict what it will do.
    Check your prediction by running the program.
2.  What is the purpose of the datetime module?
    (HINT: Read this article https://www.w3schools.com/python/python_datetime.asp,
    which is also linked on Google Classroom)
3.  What does this line of code do?
    start_time = dt.datetime.now()

4.  What does this line of code do?
    elapsed_time = end_time - start_time
'''

import datetime as dt

start_time = dt.datetime.now()
input("Press enter after 10 seconds.")
end_time = dt.datetime.now()
elapsed_time = end_time - start_time

if elapsed_time.seconds == 10:
    print("Spot on!")
elif elapsed_time.seconds > 10:
    print("You waited too long.")
elif elapsed_time.seconds < 10:
    print("You didn't wait long enough.")