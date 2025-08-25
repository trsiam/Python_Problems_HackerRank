#https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true

import string

n=int(input())
alpha=string.ascii_lowercase
width=4*n-3
rows=[]

for i in range(n):
    left=[alpha[n-1-j] for j in range(i+1)]
    right=left[:-1][::-1]
    row="-".join(left+right)
    rows.append(row.center(width,"-"))

art=rows+rows[-2::-1]
print("\n".join(art))

        