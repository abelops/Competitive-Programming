inp = int(input().split(" ")[1])

subs = sorted(list(map(lambda a: int(a), input().split(" "))))

tot = 0
for i in subs:
    tot+=i*inp
    if inp > 1:
        inp-=1
print(tot)
