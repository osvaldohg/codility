# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
# https://codility.com/programmers/lessons/9-maximum_slice_problem/max_profit/
# by oz


def solution(A):
    # write your code in Python 2.7
    if len(A)==0:
        return 0
        
    min=A.pop(0)
    res=0
    
    for num in A:
        if num < min:
            min=num
        
        tmp=num-min
        if tmp > res:
            res=tmp
            
    return res