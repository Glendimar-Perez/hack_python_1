"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    vowels = {'a': '@', 'e': '3', 'i': '1', 'o': '0', 'u': '$'}
    encrypt = ''
    for char in result:
        if char.lower() in vowels:
            encrypt += vowels[char.lower()]
        else:
            encrypt += char
    return encrypt