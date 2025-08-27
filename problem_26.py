#https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true

# from itertools import product

# A=list(input().split())
# B=list(input().split())

# for pair in product(A,B):
#     print(f"({pair[0]},{pair[1]})")


# from itertools import product

# A = list(input().split())
# B = list(input().split())

# for pair in product(A, B):
#     print(f"({pair[0]},{pair[1]})")


from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in list(product(A,B)):
    print(i, end = ' ')


  
# from itertools import product

# # Input lists A and B
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# # Compute the Cartesian product and print the result on a single line
# result = product(A, B)
# output = ' '.join(f"({x}, {y})" for x, y in result)
# print(output)
