def checkPrime(number):
    if number <= 1:
        return False
    for x in range(2, number):
        if number % x == 0:
            return False
    else:
        return True

def primenumbers(n):
    primenumbers = []
    if isinstance(n,int):
        if n >= 0:
            for x in range(2, n):
                if(checkPrime(x)):
                    primenumbers.append(x)
            return primenumbers
        else:
            raise ValueError
    else:
        raise TypeError  
#print(primenumbers(56))		