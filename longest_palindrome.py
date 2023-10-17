
# the solution provided here is O(n*2) so I don't know if there is something better but hey I am not complaing 
def LPS(s:str) -> str:
    t,ans="",""
    size=0
    for i in range(len(s)):
        for j in range(i,len(s)):
            t+=s[j]
            if t==t[::-1] and len(t)>size:
                ans=t
                size=len(t)
        t=""
    return ans


if __name__ == '__main__':
    s = "babad"
    print(LPS(s))
