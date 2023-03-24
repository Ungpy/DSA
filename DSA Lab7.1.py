from time import time

def summation1(n):
    sumary = 0
    for i in range(1,n+1):
        sumary += i
    return sumary

def summation2(n):
    sumary = n*(n+1)/2
    return sumary

def analyze_algo(n):
    stime = time()
    summation1(n)
    etime = time()
    elapsed = etime - stime
    print("execution time summation1: ", elapsed)

    stime = time()
    summation2(n)
    etime = time()
    elapsed = etime - stime
    print("execution time summation2: ", elapsed)

analyze_algo(100000)