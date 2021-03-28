
def toplaRecursive(n):
    if n == 1:
        return 1
    else:
        return toplaRecursive(n-1)+n

def Faktoriyel(n):
    if n== 0 | n==1:
        return 1
    else:
        return Faktoriyel(n-1) * n
memo ={}
def Fibonac(n):    
    if n==0 or n==1:
        return 1
    if n not in memo.keys():
        memo[n] = Fibonac(n-1) + Fibonac(n-2)
    return memo[n]

def Fibonac_rec(n):
    if n==0 or n==1:
        return 1
    return Fibonac_rec(n-1)+Fibonac_rec(n-2)

def Fib_iter(n):
    if n ==0:
        return 0
    sol = 0
    sag = 1

    for i in range(1,n):
        sol,sag = sag, sol+sag
    return sag
        
if __name__ == '__main__':
   #print(toplaRecursive(5))
   #print(Faktoriyel(5))
   # print(Fibonac(5))
   # print(Fibonac(4))
   # print(Fibonac(3))
   # print(Fibonac(2))
   # print(Fibonac(1))
   # print(Fibonac(100))
   # print(Fibonac_rec(5))
   # print(Fibonac_rec(4))
   # print(Fibonac_rec(3))
   # print(Fibonac_rec(2))
   # print(Fibonac_rec(1))
   # print(Fibonac_rec(50))
   print(Fib_iter(5000))