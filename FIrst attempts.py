import random
import math
import copy
import timeit



#insertion sort algorithm

def insertionsort(I):
    for j in range(1, len(I)):
        k = I[j]
        i = j-1
        while i>=0 and k < I[i]:
            I[i+1] = I[i]
            i = i-1
            I[i+1] = k

#merge sort

def merge(A,p,q,r):
 
    K1 = []
    K2 = []
    i = 0
    j = 0
    while i<(q-p): 
        K1.append(i)
        K1[i] = A[p+i]
        i = i+1
    while j<(r-q): 
        K2.append(j)
        K2[j] = A[q+j]
        j = j+1
  
    i=0
    j=0
    k=p
    while k>=p and k<r:
        while i<len(K1) and j<len(K2):
            if K1[i] < K2[j]:
                A[k] = K1[i]
                i = i+1
            else:
                A[k] = K2[j]   
                j = j+1
            k = k+1
        while i<len(K1):
            A[k] = K1[i]
            i = i+1
            k = k+1
        while j<len(K2):
            A[k] = K2[j]
            j = j+1
            k = k+1
    
    
def merge1(A, r1, r2):
   
    if r1<(r2-1):
       r = int(math.floor((r1+r2)/2))
       merge1(A,r1,r)
       merge1(A,r,r2)
       merge(A,r1,r,r2)
      


def mergesort(M):
    merge1(M,0,len(M))


#bubblesort


def bubblesort(B):
    b = 0
    for i in range(0,len(B)-1):
        j = len(B)-1
        while j>i:
            if B[j]<B[j-1]:
                b = B[j]
                B[j] = B[j-1]
                B[j-1] = b
            j = j-1

#python sort

def pysort(P):
    P.sort()





def Timer(function,l):
    L=[]
    random.seed(0)
    for i in range(l):
        L.append(i)
        L[i] = random.randint(-100,100)
    start = timeit.default_timer()
    function(L)
    stop =  timeit.default_timer()
    print stop-start

def Timecompare(f1,f2,l):
    print " "
    print "length"
    print l
    print (f1) 
    Timer(f1,l)
    print (f2) 
    Timer(f2,l)


Timecompare(mergesort, pysort, 1000) 
Timecompare(mergesort, pysort, 2000)
Timecompare(mergesort, pysort, 3000)
Timecompare(mergesort, pysort, 4000)
Timecompare(mergesort, pysort, 5000)
Timecompare(mergesort, pysort, 6000)
Timecompare(mergesort, pysort, 7000)
Timecompare(mergesort, pysort, 8000)
Timecompare(mergesort, pysort, 9000)
Timecompare(mergesort, pysort, 10000)

def Listcopy(L):
    K=[]
    for i in range(len(L)):
        K.append(i)
        K[i]= L[i].copy()
    return K
    
def worsttimecompare(f1,f2,l):
    L=[]
    random.seed(0)
    
    K=copy.copy(L)
    print " "
    print "worst time compare: length"
    print l
    start = timeit.default_timer()
    f1(L)
    stop =  timeit.default_timer()
    print (f1)
    print stop - start
    start = timeit.default_timer()
    f2(K)
    stop =  timeit.default_timer()
    print (f2)
    print stop - start
    
    
worsttimecompare(mergesort, pysort, 1000) 
worsttimecompare(mergesort, pysort, 2000)
worsttimecompare(mergesort, pysort, 3000)
worsttimecompare(mergesort, pysort, 4000)
worsttimecompare(mergesort, pysort, 5000)
worsttimecompare(mergesort, pysort, 6000)
worsttimecompare(mergesort, pysort, 7000)
worsttimecompare(mergesort, pysort, 8000)
worsttimecompare(mergesort, pysort, 9000)
worsttimecompare(mergesort, pysort, 10000)
    
