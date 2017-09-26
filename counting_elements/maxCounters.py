# https://codility.com/programmers/lessons/4-counting_elements/max_counters/
# by oz

def solution(N, A):
    # write your code in Python 2.7
    result=[0 for x in range(N)]
    m=0
    current=0
    same=False
    
    for op in A:
        if op <=N:
            if m > result[op-1]:
                result[op-1]=m
                
            result[op-1]+=1
            if  current < result[op-1]:
                current=result[op-1]
        else:
            m=current
                    
    for i in range(N):
        if result[i]<m:
            result[i]=m
                
    
    
    return result