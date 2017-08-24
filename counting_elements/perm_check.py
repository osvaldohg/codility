# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
# https://codility.com/programmers/lessons/4-counting_elements/perm_check/
# by oz

def solution(A):
    # write your code in Python 2.7
    
    vals=[0 for x in range(len(A))]
    
    for num in A:
        if num <= len(A):
            if vals[num-1]==0:
                vals[num-1]=1
            else:
                return 0
        else:
            return 0
            
    return 1