#https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true


# A=[]
# temp_V=-float('inf')
# temp_Vtwo=-float('inf')
# temp_Vthree=None
# for _ in range(int(input())):
#     name=input()
#     marks=float(input())
#     A.append({name:marks})


# for i in range(len(A)):
#     if(temp_V <= list(A[i].values())[0]):
#             temp_V=list(A[i].values())[0]


# for i in range(len(A)):
#      if(temp_V > list(A[i].values())[0]):
#           if(temp_Vtwo < list(A[i].values())[0]):
#                 temp_Vtwo= list(A[i].values())[0]
#                 temp_Vthree=None
#           elif(temp_Vtwo == list(A[i].values())[0]):
#                temp_Vthree=list(A[i].values())[0]



# printed_Names=set()
# for i in range(len(A)):
#      c_Marks=list(A[i].values())[0]
#      c_Names=list(A[i].keys())[0]
#      if c_Marks == temp_Vtwo or c_Marks == temp_Vthree:
#           if c_Names not in printed_Names:
#                print(c_Names)
#                printed_Names.add(c_Names)

            


# John
# 75
# Alice
# 85
# Bob
# 90
# Charlie
# 85
# Diana
# 90


# for i in range(len(A)):
#     if(temp_Vtwo<)

A = []
temp_V = float('inf')
temp_Vtwo = float('inf')


for _ in range(int(input())):
    name = input()
    marks = float(input())
    A.append({name: marks})

for i in range(len(A)):
    if(temp_V >= list(A[i].values())[0]):
        temp_V = list(A[i].values())[0]


for i in range(len(A)):
    if(temp_V < list(A[i].values())[0] <= temp_Vtwo):
        temp_Vtwo = list(A[i].values())[0]


printed_Names = set()
second_lowest_names = []

for i in range(len(A)):
    c_Marks = list(A[i].values())[0]
    c_Names = list(A[i].keys())[0]
    if c_Marks == temp_Vtwo:
        if c_Names not in printed_Names:
            second_lowest_names.append(c_Names)
            printed_Names.add(c_Names)


second_lowest_names.sort()


for name in second_lowest_names:
    print(name)
