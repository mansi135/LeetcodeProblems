# PRAMP interview

def bracket_match(text):
    # brackets = []
    c = 0
    o = 0

    for char in text:
        if char == '(':
            o += 1
        else:
            if char == ')':
                if o > 0:
                    o -= 1
                else:
                    c += 1

    return o + c