# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
# https://codility.com/programmers/lessons/7-stacks_and_queues/brackets/
# by oz

def solution (S):
    brackets={"}":"{",")":"(","]":"["}
    
    stacks=[]
    
    if len(S)==0:
        return 1

    if S[0] in brackets.keys():    
        #print "lol"
        return 0
    
    for i in S:
        if i not in brackets:
            stacks.append(i)
        else:
            val=brackets.get(i)
            if len(stacks)!=0:
                last=stacks.pop()
                if last != val:
                    return 0
            else:
                return 0
    if len(stacks)==0:
        return 1
    
    return 0
    
lol="()({}[({{{}}})])"
lol2=")())))"
print solution(lol2)