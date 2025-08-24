#https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true


# number=int(input())
# # number="1010"

# # num=int(number,2)
# # print(num)


# for i in range(1,number+1,1):
#     line=oct(i)[2:]
#     line_Two=hex(i)[2:]
#     line_Three=bin(i)[2:]
#     print(i, line,line_Two,line_Three)



# def print_formatted(number):
#   for i in range(1,number+1,1):
#     line=oct(i)[2:]
#     line_Two=hex(i)[2:]
#     line_Three=bin(i)[2:]
#     print(f"{i:<5}{line:<5}{line_Two:<5}{line_Three:<5}")
# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)




# number=int(input())
# for i in range(1,number+1,1):
#     dec=str(i).rjust(5)
#     line=oct(i)[2:].rjust(5)
#     line_Two=hex(i)[2:].rjust(5)
#     line_Three=bin(i)[2:].rjust(5)
#     print(dec, line,line_Two,line_Three)

def print_formatted(number):
    width=len(bin(number)[2:])
    for i in range(1,number+1):
        dec=str(i).rjust(width)
        line=oct(i)[2:].rjust(width)
        line_Two=hex(i)[2:].upper().rjust(width)
        line_Three=bin(i)[2:].rjust(width)
        print(dec, line,line_Two,line_Three)
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)




