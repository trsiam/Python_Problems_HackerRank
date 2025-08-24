#https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true


    
import textwrap
def wrap(string, max_width):
    para=""
    for i in range(0,len(string),max_width):
        text=string[i:i+max_width]
        para+=text+"\n"
        
    return para

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)




























