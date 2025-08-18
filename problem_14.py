#https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

def swap_case(s):
    Text=""
    for i in range(len(s)):
        if(s[i].isupper()):
            Text+=s[i].lower()
        elif(s[i].islower()):
            Text+=s[i].upper()
        else:
            Text+=s[i]
    return Text



text=input()
print(swap_case(text))
