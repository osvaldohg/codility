# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
#Find an index in an array such that its prefix sum equals its suffix sum.
#codility demo
#by oz

def solution(A):
    # write your code in Python 2.7
    total=0
    for i in range(0,len(A)-1):
        total+=A[i]
    
    if total == 0:
        return len(A)-1
    else:
        total+=A[len(A)-1]
    
    
    halfa=A[0]
    halfb=total-A[0]
    
    if halfb==0:
        return 0
    
    for i in range(1,len(A)):
        halfb-=A[i]
        if halfa==halfb:
            return i
        else:
            halfa+=A[i]
    
    return -1            