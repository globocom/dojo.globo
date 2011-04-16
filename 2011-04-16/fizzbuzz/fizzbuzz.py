# coding: utf-8


def fizzbuzz(n):
    if n <= 0:
        raise ValueError("Só existe fizzbuzz para maiores que 0")

    eh_divisivel_3 = n % 3 == 0
    eh_divisivel_5 = n % 5 == 0
    
    if eh_divisivel_3 and eh_divisivel_5:
        return 'fizzbuzz'
    if eh_divisivel_3:
        return 'fizz'
    if eh_divisivel_5:
        return 'buzz'
    
    return str(n)
    
def monta_lista(n):
    return [fizzbuzz(i+1) for i in range(n)]
