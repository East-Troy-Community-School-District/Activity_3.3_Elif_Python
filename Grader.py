'''
Grader
Pawelski
10/8/2023
Introduction to Computer Science

Instructions:
1.  Predict what the program will do before you run it.
    Check your prediction by running the program a few
    times and entering a variety of values.
2.  What does this line of code calculate?
    percentage = points_earned / total_points * 100

3.  Try entering -2 and 10 for the points earned and total points
    respectively. What grade was displayed? This makes no sense in
    the context of program (you can't get negative points on an
    assignment). Modify the program so that any negative scores
    are reported as invalide.
'''

points_earned = int(input("Enter your points you earned on the assignment >> "))
total_points = int(input("Enter the total points you could have earned on the assignment >> "))
percentage = points_earned / total_points * 100
if percentage >= 90:
  print("A")
elif percentage >= 80:
  print("B")
elif percentage >= 70:
  print("C")
elif percentage >= 60:
  print("D")
else:
  print("F")