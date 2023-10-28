memo = {}
powers = [1] * len(s)
for i in range(1, len(s)):
powers[i] = powers[i-1] * power
def hasher(start):
cur = 0
for i in range(k):
cur += (ord(s[i]) - 97+1) * powers[i]
return cur
def adder(prev, i):
prev -= (ord(s[i-k]) - 97+1)
prev//=power
prev += (ord(s[i]) - 97 +1) * powers[k-1]
return prev
cur = hasher(0)
if cur%modulo == hashValue:
return s[:k]
for i in range(k,len(s)):
cur = adder(cur, i)
if cur%modulo == hashValue:
return s[i-k+1:i+1]