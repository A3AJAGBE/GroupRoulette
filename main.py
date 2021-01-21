"""
A program that select a random name from a list of names.
The name selected will be the chosen one for the required activity.
"""
# Import random to randomize
import random

# Set a random seed
num_people = int(input("How many people are in the group? \n"))
random.seed(num_people)

# Split string method
name_submission = input("Submit everybody's name, separated by a comma and space e.g. 'John, Anna'. \n").title()
names = name_submission.split(", ")

