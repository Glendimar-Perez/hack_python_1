"""
list: [1,3,5,7,9] output => [3,5,7]
"""

def fn_hack_8():
    data = [1,3,5,7,9]
    goal = [3,5,7]
    result = []
    for item in data:
        if item in goal:
            result.append(item)
    return result