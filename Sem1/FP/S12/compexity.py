'''
n - input size
T(n) - number of operations for input size "n"
O(n) -> high bound
Omega(n) -> low bound
Teta(n)
BC - best case
WC - worst case
AC - average case


ex 1
found = false;
for (int i = 1; i<=n; ++i)
    if (x[i] == a)
        found = true;

T(n) = sum(i=1,n)1 = n apartine O(n) apartine Omega(n) => teta(n)


ex 2
found = false;
while (found == false)
    if (x[i] == a)
        found = true;

BC(T(n)): T(n) = 1
WC(T(n)): T(n) = n
AC(T(n)): T(n) = (1+2+3+4+...+n)/n = n(n+1)/2n = (n+1)/2 apartine Teta(n)


ex 3

s = 0;
for(int i = 1; i <= n*n; ++i)
{
    int j = i;
    while(j != 0)
    {
        s = s + j;
        j--;
    }
}

T(n) = sum(i=1,n^2)i = 1+2+...+n^2 = n^2(n^2+1)/2 apartine O(n^4)
n = 10 -> 1 sec  -> T(n)
n = 20 -> 16 sec -> T(2n)



ex 4
for(int i = 1; i<= n*n; ++i)
{
    for(int j = 1; j <= 100000000; ++j) # constant time so 1
        ...
}

ex 5
def f2(l):
    sum = 0
    for el in l:
        j = len(l)
        while j>1:
            sum += el*j
            j = j//3
    return sum

n = len(l)
T(n) = sum(i=1,n)log3(n) = nlog3(n)


ex 6
def sumaR(l):
    if l == []
        return 0
    if len(l) == 1:
        return l[0]
    m = len(l)//2
    return sumaR(l[:m]) + sumaR(l[m:])

T(n) = 1, n<=1
       2 * T(n/2) + n, n > 1   /+1
                    ^
                 memcopy
T(n) = 2T(n/2) + n = 2[2T(n/4) + n/2] + n = 2^2T(n/2^2) + n + n = ... = 2^k * 1 + k*n = n + nlog2(n)
 apartine O(nlog2(n))
2^k = n

'''

