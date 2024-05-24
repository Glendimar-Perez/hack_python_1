"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    vowels = {'a': '@', 'e': '3', 'i': '1', 'o': '0', 'u': '$'}
    encrypt = []
    for char in result:
        if char.lower() in vowels:
            encrypt += vowels[char]
        else:
            encrypt += char.upper()
    return encrypt