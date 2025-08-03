'''
Students of District College have subscriptions to English and French newspapers. Some students have subscribed to English only, some have subscribed to French only, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to either the English or the French newspaper but not both.


'''


# english=int(input())
# english_No=[]
# english_No=set()
# for i in range(english):
#     temp_V=input(i+1)
#     english_No.add(temp_V)


# french=int(input())
# french_No=[]
# french_No=set()
# for i in range(french):
#     temp_Vtwo=input(i+1)
#     french_No.add(temp_Vtwo)

# temp_vthree = english_No.symmetric_difference(french_No)

# temp_Vfour=len(temp_vthree)
 
# print(temp_Vfour)



english=int(input())
english_No=[]
english_No=input().split()
english_No=set(english_No)

french=int(input())
french_No=[]
french_No=input().split()
french_No=set(french_No)

temp_vthree = english_No.symmetric_difference(french_No)

temp_Vfour=len(temp_vthree)
 
print(temp_Vfour)