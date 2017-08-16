# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
#https://codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/
#by oz

def solution(A):
    # write your code in Python 2.7
    # used (n*(n+1)) /2
    
    if len(A)==0:
        return 1
    
    sum =0
    for i in A:
        sum+=i
    
    n=len(A)+1
    
    return ((n*(n+1))/2 ) - sum