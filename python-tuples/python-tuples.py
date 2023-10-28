def getHash():
    inp1 = input()
    inp2 = tuple(map(lambda a: int(a), input().split(" ")))
    print(hash(inp2))
if __name__ == '__main__':
    getHash()
