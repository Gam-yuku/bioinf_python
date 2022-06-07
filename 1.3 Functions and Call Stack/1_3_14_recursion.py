#1,1,2,3,5,8... последовательность фибоначи. fib(4) = 2 + 3
#fib(k) = 1; k = 0, k =1  (fib(k) - сумма)
#fib(k) = fib(k-1) + fib(k+1)

def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

y = fib(5)
print(y)