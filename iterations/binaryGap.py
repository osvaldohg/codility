# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
#https://codility.com/programmers/lessons/1-iterations/
#by oz

def solution(N):
    # write your code in Python 2.7
    maxgap=0
    zeros=0
    binary=bin(N)
    for i in range(2,len(binary)):
        if binary[i]=="0":
            zeros+=1
        else:
            if zeros>maxgap:
                maxgap=zeros
            zeros=0
           
    return maxgap

#main    
n=int(raw_input().strip())
print solution(n)