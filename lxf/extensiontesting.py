# start

def adding (a,b):
    """adding two numbers

    Args:
        a (int): number a
        b (int): number b

    Returns:
        int: total number
    """
    return a+b


print (adding(1,1))





L = ['1','2','3']

def strltointl(l):
    """ make a str list into int list

    Args:
        l (list): input str list

    Returns:
        list: output int list
    """
    ln = []
    for n in l:
        ln.append(int (n)) 
    return ln

Ln = strltointl(L)

print (Ln)

print ('hello')