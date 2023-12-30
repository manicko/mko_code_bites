def sieve(n):
    z = {2} # set of primes
    N = {x for x in range(3,n+1,2)} # natural numbers in range.
    size = len(N)
    while size>0: # stop when N is exhausted.
        sn = min(N) # sn: smallest number in N
        #print ('n=',sn)
        for i in z:
            if sn%i == 0: # it is divisible with a prime and cannot be a prime.
                m = {n for n in range(sn,n+1,sn)} # m is set of multiples of sn
                N = N - m # using deduction of sets to update N
            elif sn<i*i: # match-point has been passed.
                z.add(sn)
                m = {n for n in range(sn,n+1,sn)} # m is set of multiples of sn
                N = N - m # using deduction of sets to update N
                break
        size=len(N)
    return z

if __name__ =='__main__':
    import time
    #start = time.clock()
    L = sieve(1000) # 104729 prime number 10,000
    #end = time.clock()
    print ('total runtime: ', L)# str(end-start))