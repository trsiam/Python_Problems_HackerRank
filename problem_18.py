#https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true


def count_substring(string, sub_string):
    line=string
    line_Two=sub_string
    count=0
    for i in range(len(line)-len(line_Two)+1):
        if(line[i:i+len(line_Two)]==line_Two):
            count+=1

    return count




string = input().strip()
sub_string = input().strip()
    
count = count_substring(string, sub_string)
print(count)