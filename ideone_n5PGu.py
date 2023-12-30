'''http://c...content-available-to-author-only...e.com/recipes/117119/'''

from itertools import count,islice,groupby
from timeit import Timer
import collections
from heapq import merge
import __main__


'''om/a/10733
Unserstanding code from here: http://stackoverflow.c621/862380
postponed sieve, by Will Ness
See also: http://i...content-available-to-author-only...e.com/WFv4f
'''        
def primes4(debug=False,level=0):
    '''The space complexity is needlessly O(n). O(sqrt(n)) is enough indeed,
    achieved by postponing the addition of stepping information for a prime
    into the dict until that prime's square is seen amongst the candidates,
    and not a moment sooner.
    Having much smaller dict, performance and empirical time complexity improve too.
    http://i...content-available-to-author-only...e.com/WFv4f'''

    name = '{0}'.format(level)
    
    #print = __builtins__.print if debug else lambda *p: None

    print('{name}: yield 2'.format(name=name)); yield 2 
    print('{name}: yield 3'.format(name=name)); yield 3
    print('{name}: yield 5'.format(name=name)); yield 5
    print('{name}: yield 7'.format(name=name)); yield 7 
    D = {}              
    c = 9; print('{name}: c = {c}'.format(name=name,c=c))
    ps = (p for p in primes4(debug=debug,level=level+1)); print('{name}: Creating subiterator'.format(name=name))
    temp = next(ps)
    print('{name}: skip {temp}'.format(name=name,temp=temp))     #skip 2 
    p = next(ps); print('{name}: p = {p}'.format(name=name,p=p)) # 3
    q = p*p; print('{name}: q = {q}'.format(name=name,q=q))      # 9
    while True:
        print('{name}: D = {D}'.format(name=name,D=D))
        if c not in D:
            print('{name}: c not in D'.format(name=name))
            if c < q:
                print('{name}: c<q'.format(name=name))
                print('{name}: yield c = {c}'.format(name=name,c=c))
                yield c 
            else:
                print('{name}: c=q'.format(name=name))
                x = add(D,c+2*p,2*p); print('{name}: D[{x}]={s}'.format(name=name,x=x,s=2*p)) 
                p = next(ps); print('{name}: p = {p}'.format(name=name,p=p))
                q = p*p; print('{name}: q = {q}'.format(name=name,q=q))
        else:
            print('{name}: c in D'.format(name=name))
            s = D.pop(c); print('{name}: popping from D: s = {s}'.format(name=name,s=s))
            x = add(D, c+s, s); print('{name}: adding to D[{x}]={s}'.format(name=name,x=x,s=c+s))
        c += 2; print('{name}: c+=2 -> c={c}'.format(name=name,c=c))


def add(D,x,s):
    while x in D:
        x += s
    D[x] = s
    return x


def main1():
    '''Just '''
    n = 20
    next(islice(primes4(debug=True), n, n), None) #consume n values     


if __name__=='__main__':
    main1()