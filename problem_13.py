#https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

N=int(input())
A=[]
for _ in range(N):
    parts=input().split()
    command=parts[0]
    if(command=="insert"):
        index=int(parts[1])
        value=int(parts[2])
        A.insert(index,value)
    elif(command =="print"):
        print(A)
    elif(command == "remove"):
        value=int(parts[1])
        A.remove(value)
    elif(command == "append"):
        value=int(parts[1])
        A.append(value)
    elif(command == "sort"):
        A.sort()
    elif(command == "pop"):
        A.pop()
    elif(command == "reverse"):
        A.reverse()


# print(command)
# print(value)