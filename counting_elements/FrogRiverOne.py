# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
# https://codility.com/programmers/lessons/4-counting_elements/frog_river_one/
# by oz

def solution(X, A):
    # write your code in Python 2.7
        
    vals=[0 for x in range(0,X+1)]
    count=0
    
    for i in range (0,len(A)):
        if vals[A[i]]==0:
            vals[A[i]]=1
            count+=1
        
        if count==X:
            return i
            
    return -1
    
        