# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
# https://codility.com/programmers/lessons/5-prefix_sums/passing_cars/
# by oz

def solution(A):
    # write your code in Python 2.7
    unos=0
    res=0
    for num in A:
        if num==1:
            unos+=1
            
    for num in A:
        if num==0:
            res+=unos
        
        if num==1:
            unos-=1
        
    if res > 1000000000:
        return -1
        
    return res