from time import time
import random
def createList(n):
    #l1, l2, l3 = list(), list(), list()
    l1 = list(random.sample(range(1,1000000), n))
    l2 = list(random.sample(range(1000001, 2000000), n))
    l3 = list(random.sample(range(2000001, 3000000), n))
    return l1,l2,l3

def isintersect1(l1, l2, l3):
    for num in l1:
        if num in l3 and num in l2:
            return True
    return False

def isintersect2(l1, l2, l3):
    dotime = 0
    for i in range(0, len(l1)):
        dotime += 1
        for j in range(0, len(l2)):
            dotime += 1
            for k in range(0, len(l3)):
                dotime += 1
                if l3[k] == l2[j] == l1[i]:
                    return True
    print(dotime)
    
    return False

def analyze_algo(n):
    #stime = time()
    l1,l2,l3 = createList(n)
    #etime = time()
    #elapsed = etime - stime
    #print("create list time: ", elapsed)

    print(n)

    stime = time()
    print(isintersect1(l1,l2,l3))
    etime = time()
    elapsed = etime - stime
    print("execution time isintersect1: ", elapsed)

    stime = time()
    print(isintersect2(l1,l2,l3))
    etime = time()
    elapsed = etime - stime
    print("execution time isintersect2: ", elapsed)

analyze_algo(10000)