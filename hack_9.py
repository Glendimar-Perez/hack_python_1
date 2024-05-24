"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    data = [1, 2, 3]
    result = []
    i = 0
    while i < len(data):
        result.append(data[i])
        result.append('@')
        i += 1
    return result