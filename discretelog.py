import math;

def powmod(x, y, p): 
    res = 1;
    x = x % p;
    while (y > 0): 
        if (y & 1): 
            res = (res * x) % p; 
        y = y >> 1;
        x = (x * x) % p; 
    return res; 
 
def discreteLogarithm(a, b, p): 
    n = int(math.sqrt(p) + 1); 
    value = [0] * p; 
    for i in range(n, 0, -1): 
        value[ powmod (a, i * n, p) ] = i; 
    for j in range(n): 
        cur = (powmod (a, j, p) * b) % p; 
        if (value[cur]): 
            ans = value[cur] * n - j; 
            if (ans < p): 
                return ans; 
    return -1; 

a = 11; 
b = 2; 
p = 1201; 
print(discreteLogarithm(a, b, p));