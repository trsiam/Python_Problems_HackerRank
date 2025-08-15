# We have seen the applications of union, intersection, difference and symmetric difference operations, but these operations do not make any changes or mutations to the set.

# We can use the following operations to create mutations to a set:

# .update() or |=
# Update the set by adding elements from an iterable/another set.

# >>> H = set("Hacker")
# >>> R = set("Rank")
# >>> H.update(R)
# >>> print H
# set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
# .intersection_update() or &=
# Update the set by keeping only the elements found in it and an iterable/another set.

# >>> H = set("Hacker")
# >>> R = set("Rank")
# >>> H.intersection_update(R)
# >>> print H
# set(['a', 'k'])
# .difference_update() or -=
# Update the set by removing elements found in an iterable/another set.

# >>> H = set("Hacker")
# >>> R = set("Rank")
# >>> H.difference_update(R)
# >>> print H
# set(['c', 'e', 'H', 'r'])
# .symmetric_difference_update() or ^=
# Update the set by only keeping the elements found in either set, but not in both.

# >>> H = set("Hacker")
# >>> R = set("Rank")
# >>> H.symmetric_difference_update(R)
# >>> print H
# set(['c', 'e', 'H', 'n', 'r', 'R']

# TASK
# You are given a set  and  number of other sets. These  number of sets have to perform some specific mutation operations on set .

# Your task is to execute those operations and print the sum of elements from set .




#Talking A set input direcly 



A_Range=int(input())
A = set(map(int, input().split()))
operation_Number=int(input())
for _ in range(operation_Number):
    operation_Name,operationset_Size=input().split()
    B = set(map(int, input().split()))
    if(operation_Name == "intersection_update"):
        A.intersection_update(B)
    elif(operation_Name == "update"):
        A.update(B)
    elif(operation_Name == "symmetric_difference_update"):
        A.symmetric_difference_update(B)
    elif(operation_Name == "difference_update"):
        A.difference_update(B)  

print(sum(A))


# A_Range = int(input())
# A = set(map(int, input().split()))

# operation_Number = int(input())
# for _ in range(operation_Number):
#     operation_Name, operationset_Size = input().split()
#     B = set(map(int, input().split()))
    
#     if operation_Name == "intersection_update":
#         A.intersection_update(B)
#     elif operation_Name == "update":
#         A.update(B)
#     elif operation_Name == "symmetric_difference_update":
#         A.symmetric_difference_update(B)
#     elif operation_Name == "difference_update":
#         A.difference_update(B)

# print(sum(A))




















