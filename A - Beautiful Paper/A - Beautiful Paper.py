test = int(input())
 
for i in range(test):
    n1 = input().split(" ")
    n1i = int(n1[0])
    n1j = int(n1[1])
 
    n2 = input().split(" ")
    n2i = int(n2[0])
    n2j = int(n2[1])
 
    
    if max(n1i, n1j) != max(n2i, n2j):
        print("No")
    elif min(n1i, n1j) + min(n2i, n2j) == max(n1i, n1j):
        print("Yes")
    else:
        print("No")