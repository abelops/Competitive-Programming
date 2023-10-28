leng = int(input())
sizes = {'S' : 1, 'M' : 2, 'L' : 3 }
for i in range(leng):
    inp = input().split(" ")
    s1 = inp[0]
    s2 = inp[1]
    if sizes[s1[-1]] > sizes[s2[-1]]:
        print(">")
    elif sizes[s1[-1]] < sizes[s2[-1]]:
        print("<")
    elif s1[-1] == s2[-1] and s1[-1] == "M":
        print("=")
    else:
        if sizes[s1[-1]] == sizes[s2[-1]] and s1[-1] == "L":
            if len(s1) > len(s2):
                print(">")
            elif len(s1) < len(s2):
                print("<")
            else:
                print("=")
        elif sizes[s1[-1]] == sizes[s2[-1]] and s1[-1] == "S":
            if len(s1) > len(s2):
                print("<")
            elif len(s1) < len(s2):
                print(">")
            else:
                print("=")
            