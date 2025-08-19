#https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true

def mutate_string(string, position, character):
    line=list(string)
    index=position
    char=character
    line[position]=char
    return  "".join(line)


line=input()
parts = input().split()
index=int(parts[0])
charecter=parts[1]

result=mutate_string(line,index,charecter)
print(result)





