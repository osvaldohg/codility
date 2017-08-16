# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
#https://codility.com/programmers/lessons/2-arrays/cyclic_rotation/
#by oz

def solution(A, K):
    # write your code in Python 2.7
    if len(A)==0:
        return []
    offset=K%len(A)
    res=[]
    for i in range(0,len(A)):
        pos=i-offset
        res.append(A[pos])
        
    return res
        
#main        
a=map(int, raw_input().strip().split())
k=int(raw_input().strip())
print solution(a,k)