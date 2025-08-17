#https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true

# A=[]
# n=int(input())
# for i in range(n):
#     data=input().split()
#     name=data[0]
#     marks=list(map(int,data[1:]))
#     A.append({name:marks})



# print(A[0]['siam'][2])
temp_V=0
n=  int(input())
students_info={}

for _ in range(n):
    name,*line=input().split()
    scores=list(map(float,line))
    students_info[name]=scores
querry_name=input()
i=1
for i in range(3):
    temp_V+=students_info[querry_name][i]

temp_Vtwo=temp_V/3
print(f"{temp_Vtwo:.2f}")
