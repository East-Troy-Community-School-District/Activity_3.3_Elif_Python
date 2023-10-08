'''
Grader
Pawelski
10/8/2023
Introduction to Computer Science

Instructions:
Run the program and try entering a variety of
numbers for the points earned and the total points
possible. What happens each time? What happens if
you try to enter text? Why does this happen?
In your own words, describe how an if/elif/else
statement works.

Let's focus on a line  for a second. Describe the steps
Python takes to execute this line. Let's now focus on line .
What does this line of code calculate?

Try entering -2 and 10 for the points earned and total points
respectively. What grade was displayed? What happens if you
enter 11 and 10 for the points earned and the total points
respectively? Why? Does this make sense in the context?
Currently, this program does not have a way for checking
invalid grades or grades above an A. Let's fix this issue with
the program.
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