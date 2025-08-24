#https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true


M,N=map(int,input().split())
for i in range(M//2):
    line=('.|.'*(2*i+1)).center(N,'-')
    print(line)

print('WELCOME'.center(N,'-'))

for i in range(M//2-1,-1,-1):
    line=('.|.'*(2*i+1)).center(N,'-')
    print(line)
    





