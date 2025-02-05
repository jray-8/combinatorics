def factorial(n):
    ''' Returns `n!` '''
    if not isinstance(n, int):
        raise TypeError('factorial() requires an integer input')
    if (n < 0):
        raise ValueError('factorial() is not defined for negatives')
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def permute(n, r=None):
    ''' `n` permute `r` (without replacement)
    
		default (r = n)
    '''
    if r is None:
        r = n
    if not isinstance(n, int) or not isinstance(r, int):
        raise TypeError('permute(n, r): input must be positive integers')
    elif (n < 0) or (r < 0):
        raise ValueError('permute(n, r): n, r >= 0')
    elif (n - r) < 0:
        raise ValueError('permute(n, r): n must be >= r')
    return int(factorial(n) / factorial(n-r))

def choose(n, r):
    ''' `n` choose `r` (without replacement) '''
    permutations = permute(n,r)
    if permutations is None:
        return None
    return int(permutations / factorial(r))

def multichoose(n, r):
    ''' Select `r` from `n` varieties (with replacement) '''
    return choose(r + n-1, r)
