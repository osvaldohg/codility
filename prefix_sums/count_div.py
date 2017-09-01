# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
# https://codility.com/programmers/lessons/5-prefix_sums/count_div/
# by oz

def solution(A, B, K):
    # write your code in Python 2.7

    start=A
    diff=0
    
    while start%K!=0:
        start+=1
        
    diff=B-start
    times=diff/K
    
    return times+1