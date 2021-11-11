"""
Given a set of activites with start time, end time, and weight, find maximum
total weight for compatible activites

Optimal substructure:
    remove an activity, e, from the solution. This is still the solution to the
    problem if e's time frame didn't exist

Need to solve by finding the best activity to fill each block of time, build up
to larger blocks

Recursive solution:
    
"""

class Activity:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

    def __str__(self):
        return f'{self.start} to {self.end}: {self.weight}'

def test():
    activites = [

    ]

def areCompatible(a1, a2):
    a1BeforeA2 = a1.end <= a2.start
    a2BeforeA1 = a2.end <= a1.start

    return a1BeforeA2 or a2BeforeA1
