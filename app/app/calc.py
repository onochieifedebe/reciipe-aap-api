"""
Calculator functions
"""

def add(*args):
    total_sum = 0
    "Add arguments and return sum"
    for arg in args:
        total_sum += arg
    return total_sum

def subtract(*args):
    total = args[0]
    
    for index in range(1,len(args)):
        total -= args[index]
    
    return total