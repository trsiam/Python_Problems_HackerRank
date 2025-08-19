#https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true

def split_and_join(line):
  temp_V=line.split(" ")
  temp_Vtwo="-".join(temp_V)

  return temp_Vtwo


line = input()
result = split_and_join(line)
print(result)
