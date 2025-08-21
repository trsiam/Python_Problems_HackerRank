#https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true



s = input()
result=False
result_O=False
result_T=False
result_Th=False
result_F=False
for i in range(len(s)):
    if(s[i].isalnum()):
        result_O=True
    if(s[i].isalpha()):
        result=True
    if(s[i].isdigit()):
        result_T=True
    if(s[i].islower()):
        result_Th=True
    if(s[i].isupper()):
        result_F=True
print(result_O)
print(result)
print(result_T)
print(result_Th)
print(result_F)
