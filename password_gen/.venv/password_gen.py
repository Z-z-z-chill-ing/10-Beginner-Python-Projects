import random

letters = set(
    [
        "a", "b", "c", "d", "e", "f", "g", "h", "k", "i", "j", "m", "n",
        "l", "o", "p", "t", "r", "p", "w", "s", "u", "q", "v", "x", "y", "z"
    ]
)

digits = set(
    [
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
    ]
)

symbols = set(
    [
        "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "œ", "∑",
        "®", "†", "¥", "¨", "ø", "π", "[", "“", "]", "\\", "«", "å", "ß", "∂", "ƒ", "©", "˙",
        "∆", "˚", "¬", ";", "…", "æ", "≈", "ç", "√", "∫", "µ", ",", "≤", ".", "≥", "/", "?"
    ]
)

def filter_func(x: str):
        x = x.lower()
        if (x == "l" or x == "d" or x == "s" or x == "upp" or x == "low"):
            return True
        else:
            return False

def generate_password(length: int, *set_restrict: str) -> str:
    """
    Generates a strong password.
    Parameter set_restrict can only take values: 
    'l' - letters, 'd' - digits, 's' - symbols, 'upp' - uppercase,
    'low' - lowercase, these values will be restricted during a creation process.
    If empty, no restrictions will be applied.
    """
    merge_set = set([])
    password = ""
    set_restrict = tuple(filter(filter_func, set_restrict))
    if (set_restrict.count("l") == 0):
        merge_set.update(letters)
    if (set_restrict.count("d") == 0):
        merge_set.update(digits)
    if (set_restrict.count("s") == 0):
        merge_set.update(symbols)
    while (not len(password) == length):
        letter = merge_set.pop()
        if (set_restrict.count("upp") == 0 and tuple(letters).count(letter) > 0):
            rand_upp = random.randint(0,1)
            if (set_restrict.count("low") > 0):
                rand_upp = 1
            if (rand_upp == 1):
                letter = letter.upper()
        password += letter
    return password

password = generate_password(0)
print(password)