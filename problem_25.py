#https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true

# pos=""
# temp=""
# text=str(input())
# temp_Two=list(text)
# temp_Three="".join(temp_Two)

# print(temp_Two)
# print(temp_Three)

# text=str(input())
# temp=list(text)
# for i in range(len(text)):
#     temp[0]=temp[0].upper()
#     if(text[i]==" "):
#         temp[i+1]=temp[i+1].upper()
    

# print("".join(temp))


# def solve(s):
#     temp = list(s.lower())
#     for i in range(len(temp)):
#         temp[0] = temp[0].upper()
#         if temp[i] == " ":
#             temp[i+1] = temp[i+1].upper()
#     return "".join(temp)

# s = input()

# result = solve(s)

# print("".join(result))



# def solve(s):
#     temp = list(s.lower())
#     for i in range(len(temp)):
#         if i == 0 and temp[i].isalpha():
#             temp[i] = temp[i].upper()
#         elif temp[i] == " " and i + 1 < len(temp) and temp[i+1].isalpha():
#             temp[i+1] = temp[i+1].upper()
#     return "".join(temp)

# s = input()
# result = solve(s)
# print(result)

def solve(s):
    for name in s.split():
        s=s.replace(name,name.capitalize())
        
    return s
