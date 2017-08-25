# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
# https://codility.com/programmers/lessons/6-sorting/distinct/
# by oz

def solution(A):
    # write your code in Python 2.7
    numlist={}
    count=0
    
    for num in A:
        if num not in numlist:
            count+=1
            numlist[num]=1
        else:
            numlist[num]+=1
            
    return count