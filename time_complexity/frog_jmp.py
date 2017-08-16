# # you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
# https://codility.com/programmers/lessons/3-time_complexity/frog_jmp/
# by oz

def solution(X, Y, D):
    # write your code in Python 2.7
    goal=Y-X
    
    if X==Y:
        return 0
        
    if goal%D==0:
        return goal/D
    else:
        return goal/D+1
    
        