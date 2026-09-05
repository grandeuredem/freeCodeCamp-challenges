import string
def is_valid_ipv4(ipv4):

    ipv4 = ipv4.split('.')
    for char in ipv4:
        if len(char) >= 2 and char.startswith('0'):
            return False
        
        for x in char:
            if x in string.punctuation:
                return False
    try:
        ipv4 = list(map(int, ipv4))
    except:
        return False
    
    if len(ipv4) != 4:
        return False
    
    for num in ipv4:
        if num < 0 or num > 255:
            return False
        
    return True

print(is_valid_ipv4('0.0.0.0'))
