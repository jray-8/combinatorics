def fact(n):
    ''' Factorial, return `n!` '''
    if not isinstance(n, int):
        raise TypeError('fact() requires an integer input')
    if (n < 0):
        raise ValueError('fact() is not defined for negatives')
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def nPr(n, r=None):
    ''' `n` Permute `r` (without replacement)
    
		default (r = n)
    '''
    if r is None:
        r = n
    if not isinstance(n, int) or not isinstance(r, int):
        raise TypeError('P(n, r): input must be positive integers')
    elif (n < 0) or (r < 0):
        raise ValueError('P(n, r): n, r >= 0')
    elif (n - r) < 0:
        raise ValueError('P(n, r): n must be >= r')
    return int(fact(n) / fact(n-r))

def nCr(n, r):
    ''' `n` choose `r` (without replacement) '''
    permutations = nPr(n,r)
    if permutations is None:
        return None
    return int(permutations / fact(r))

def multichoose(n, r):
    ''' `n` multichoose `r` (with replacement)
    
		select `r` from `n` varieties
    '''
    return nCr(r + n-1, r)
