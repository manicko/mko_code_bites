import re
# input: My dear, here we must run as fast as we can, just to stay in place. And if you wish to go anywhere you must run twice as fast as that.
s = re.sub(r'[.,!?:;]', '', input().lower()).split()
d = {}
for w in s:
    d[w] = d.get(w, 0) + 1

res = min(d, key=lambda x: (d[x], x))

print(res)
