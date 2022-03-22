#x is the input number
def isPalindrome(x):
    x = list(str(x))
    for i in range(int(len(x)/2)):
        if x[i] != x[- i - 1 ]:
            return False    
    return True
