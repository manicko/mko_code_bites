
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # check if s present in (s+s)[1:-1]
        # if s is a repeats of subs, then s = subs*k, now k >=2 or else
        # s doesn't have this property
        
        # so, IF s has repeats, k >= 2
        # since k>=2, 2*s has 2k repeats of subs, removing head and tail
        # leaves us with 2k-2 repeats, 2k-2 >= k if k >= 2, thus s 
        # must be inside (s+s)[1:-1]
        
        # IF s has no repeats, k == 1, s = 1*subs, while subs == s
        # so 2*s = 2*subs, removing heads and tails must give us 0*subs
        # 2k-2 = 0, thus s cannot be inside (s+s)[1:-1]
        # Now, if you say, what if by shifting, within (s+s)[1:-1]
        # there is 1 repeat, see below illustration:
        # assume s is made up of [..A..][.B.], no repeats, so A != B
        # and B not in A.
        # 2*s= [..A..][.B.][..A..][.B.]
        # if we remove head and tail:
        # 2*s[1:-1] = [.A..][.B.][..A..][.B]   , then no matter where you put s to fit
        #               [..A..][.B.],  then we're saying: slicing first few letters of A
        # and adding these letters to B's tail, will give you original s
        # [a1 a2 a3 a4] [a5 a6], 'an' are chars
        # [a3 a4 a5 a6] [a1 a2]. These should match, giving us
        # a1=a5=a3; a2=a6=a4; so a1a2 = a3a4 = a5a6, there are repeats.
        # if we have odd chars
        # [a1 a2 a3 a4] [a5]
        # [a3 a4 a5] [a1 a2]
        # then a1=a3=a4; a2=a4=a5; so everybody equal.
        
        return s in (2*s)[1:-1]
        
sol=Solution()
s = "bb"

res = sol.repeatedSubstringPattern(s)
print(res)


s = "bbfcbbbbfcbb"
print(s)
ss=s+s 
print(ss)
ss1=ss[1:-1]

print(ss1)
