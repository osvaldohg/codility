# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
#https://codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/
#by oz

def solution(A):
    # write your code in Python 2.7
    res=0
    
    for i in A:
        res=res^i
    
    return res
    
