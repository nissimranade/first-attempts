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

#start = timeit.default_timer()    
#insertionsort(I)
#stop = timeit.default_timer()
#print "Insertion sort"
#print I

#print stop - start

#merge sort algorithm


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
    
    
def mergesort(A, r1, r2):
   
    if r1<(r2-1):
       r = int(math.floor((r1+r2)/2))
       mergesort(A,r1,r)
       mergesort(A,r,r2)
       merge(A,r1,r,r2)
      
#start = timeit.default_timer()

#mergesort(M,0,len(M))

#stop = timeit.default_timer()

#print "Merge sort"
#print M
#print stop - start



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

def merge1(M):
    mergesort(M,0,len(M))

#start = timeit.default_timer()    
#bubblesort(I)                
#stop = timeit.default_timer()

#print "Bubble sort"        
#print B
#print stop - start

#start = timeit.default_timer()
#P.sort()
#stop = timeit.default_timer()

#print "Python sort"
#print P
#print stop - start

def Timer(function,l):
    L=[]
    for i in range(l):
        L.append(i)
        L[i] = random.randint(-100,100)
    start = timeit.default_timer()
    function(L)
    stop =  timeit.default_timer()
    print stop-start
 

Timer(merge1, 100)





