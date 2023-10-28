import textwrap

def wrap(string, max_width):
    ans = ""
    for i in range(0,len(string),max_width):
        ans+= "".join(string[i:i+max_width])
        ans+="\n"
    return ans

if __name__ == '__main__':