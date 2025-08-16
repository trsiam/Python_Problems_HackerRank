#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

# import array as arr

# temp_V=0
# temp_Vtwo=0
# n=int(input())
# A=arr.array('i',map(int,input().split()))
# for i in range(n):
#     if(A[i] >= temp_V):
#         temp_V=A[i]

# for i in range(n):
#      if(temp_V != A[i]):
#         if(A[i]>= temp_Vtwo):
#             temp_Vtwo=A[i]


# print(temp_Vtwo)

# temp_V=-float('inf')
# temp_Vtwo=-float('inf')
# n=int(input())
# A=list(map(int,input().split()))

# for i in range(n):
#     if(A[i] >= temp_V):
#         temp_V=A[i]

# A=[score for score in A if score != temp_V]

# for i in range(len(A)):
#      if(temp_V != A[i]):
#         if(A[i]>= temp_Vtwo):
#             temp_Vtwo=A[i]


# print(temp_Vtwo)



# temp_V = -float('inf')
# temp_Vtwo = -float('inf')
# n = int(input())
# A = list(map(int, input().split()))

# for i in range(n):
#     if A[i] >= temp_V:
#         temp_V = A[i]

# A = [score for score in A if score != temp_V]

# for i in range(len(A)):
#         if A[i] >= temp_Vtwo:
#             temp_Vtwo = A[i]
    

# print(temp_Vtwo)




temp_V=-float('inf')
temp_Vtwo=-float('inf')
n=int(input())
A=list(map(int,input().split()))

for i in range(n):
    if(A[i] >= temp_V):
        temp_V=A[i]

for i in range(len(A)):
     if(temp_V != A[i]):
        if(A[i]>= temp_Vtwo):
            temp_Vtwo=A[i]


print(temp_Vtwo)
