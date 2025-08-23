#https://www.hackerrank.com/challenges/text-alignment/problem?isFullScreen=true

# width=10
# print("Hacker".ljust(width,'-'))

width=int(input())
for i in range(1,width*2,2):
    row="".join ("H"*i)
    print(row.center(width * 3))

for i in range(width+1):
    row="".join("H"*width)
    print(row.center(width*3) + row.rjust(width*5))

for i in range(3):
    row="".join("H"*(width*8+5))
    print(row.center((width*((width*2)+1))))

for i in range(width+1):
    row="".join("H"*width)
    print(row.center(width*3) + row.rjust(width*5))

for i in range(width*2-1,0,-2):
    row="".join ("H"*i)
    print(row.center(width * (width*3)))
   


    

    
   





























