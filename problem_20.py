#https://www.hackerrank.com/challenges/text-alignment/problem?isFullScreen=true

# width=10
# print("Hacker".ljust(width,'-'))

width=int(input())
c='H'
for i in range(width):
    print((c*i).rjust(width-1)+c+(c*i).ljust(width-1))

for i in range(width+1):
    print((c*width).center(width*2)+(c*width).center(width*6))

for i in range((width+1)//2):
    print((c*width*5).center(width*6))


for i in range(width+1):
    print((c*width).center(width*2)+(c*width).center(width*6))

for i in range(width):
    line=((c*(width-i-1)).rjust(width)+c+(c*(width-i-1)).ljust(width))
    print(line.rjust(width*6))


   





























