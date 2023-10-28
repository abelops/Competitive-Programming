def swap_case(s):
    a = ""
    for i in s:
        if i.isupper():
            a+=i.lower()
        else:
            a+=i.upper()
    return a

if __name__ == '__main__':