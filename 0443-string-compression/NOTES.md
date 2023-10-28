class Solution:
def compress(self, chars: List[str]) -> int:
l = 0
r = 1
leng = len(chars)
while r < leng:
if r >= len(chars):
break
if chars[l] == chars[r]:
r+=1
else:
if r-l == 1:
l+=1
r+=1
elif r-l > 1:
count = 0
for i in range(l+1, r):
print(l,r,i,chars)
if chars[l] != chars[r-1]:
break
chars.pop(r-1)
count+=1
r-=1
if count+1 > 9:
for i in range(len(str(count+1))):
chars.insert(l+1+i, str(count+1)[i])
r+=1
else:
chars.insert(l+1, str(count+1))
r+1
l+= r-l
r+=1
print(chars,l,r)
r = len(chars)-1
if r-l == 0:
return len(chars)
for i in range(r-l):
chars.pop()
if r-l+1 > 9:
for i in range(len(str(r-l+1))):
chars.append(str(r-l+1)[i])
else:
chars.append(str(r-l+1))
return len(chars)