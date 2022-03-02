def code_block(one, two):
    if one in two:
        return two
    elif two in one:
        return one
    else:
        overlap_1 = 0
        overlap_2 = 0
        if len(one) < len(two):
            for every in range(len(one)):
                if compare(one[-every:], two[:every]):
                    overlap_1 = every
                elif compare(one[:every], two[-every:]):
                    overlap_2 = every
        else:
            for every in range(len(two)):
                if compare(two[-every:], one[:every]):
                    overlap_2 = every
                elif compare(two[:every], one[-every:]):
                    overlap_1 = every
        if overlap_1 > overlap_2:
            return one+two[overlap_1:]
        elif overlap_1 < overlap_2:
            return two+one[overlap_2:]
        else:
            return one + two
    
if '__name__' == '__main__':
    import random
    import string
  
    var1 = "".join([random.choice(string.ascii_lowercase) for _ in range(random.randint(1, 100))])
    var2 = "".join([random.choice(string.ascii_lowercase) for _ in range(random.randint(1, 100))])
    response = code_block(var1, var2)
