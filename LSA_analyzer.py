from time import time
from functools import reduce
import random
from math import gcd


def co_primes(n):
    for i in range(1, n):
        if gcd(i,n) == 1:
            yield i
            
def possibilities():
    C_n = []
    for _ in range(10000-1052):
        sums = []
        for j in range(1, 256):
            k = random.choice(range(1052, 1052 + 10000))
            c = co_primes(k)
            s = reduce(lambda x,y: x*y%k, [next(c) for _ in range(j)])
            sums.append(s)
        C_n.append(sums)
     
    
    l = C_n[random.choice(range(100))]
    l_4 = []
    for value in l:
        num = 0
        #print(value)
        indexes = []
        for l in C_n:
            if value in l:
                if l.index(value) not in indexes:
                    #print(l.index(value))
                    num += 1
                    indexes.append(l.index(value))
                
        l_4.append((value, num))
    
    s = 0
    for l in l_4:
        s+= l[1]
    print(f'Average of possibilities: {s/len(l_4)}')
    return l_4
    #print(num)
    #print()

def histo(encryption):
    import matplotlib.pyplot as plt
    #data = [abs(j[0]) for j in encryption]
    #data = [abs(j[0]) for j in encryption]
    data = sorted(encryption)
    plt.bar(range(len(encryption)), data, align='center')
    plt.xticks(range(len(encryption)), data)
    plt.show()
    print(data)
    return

def uniq(encryption):
    key = set()
    for t in encryption:
        key |= {t}
    uniq =  len(key)
    print('Len(keys) =', uniq)
    return uniq

def sigma_finder(k):
    l = list(co_primes(k))
    c = reduce(lambda x,y: x*y % k, l)
    _, z, _ = gcdExtended(c, k)
    for i in range(1, len(l)):
        c = reduce(lambda x,y: x*y % k, l[:i])
        if z*c%k == 1:
            print(i)
        

def match(string1, string2):
    if len(string2) != len(string1):
        print("Strings lengths don't match!")
        return
    c = 0
    ctr = 0
    l = []
    for i,j in zip(string1, string2):
        if i!=j:
            print(f'{i} should have been {j}')
            l.append(c)
            ctr += 1
        c += 1
    print(ctr)
    print(l)
    
    print(f'Error Perecentage = {ctr/len(string2)*100}%')







