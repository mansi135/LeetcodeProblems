# is a string containing just '(' or ')'. For example it could be ((())) or (()()()) or ((() or )(()
# Check if the string contains 'matched' paranthesis (matched as in it would be mathematically correct use of paranthesis). For example the last two examples aren't matched
# Hint: Use the list methods append and pop. You can also read about "Stack datastructure" online
def is_paranthesis_matched(str):
    l=[]
    #flag=True
    for s in str:
        if s=='(':
            l.append(s)
        elif s==')':
            if len(l)>0:
                l.pop()
            else:
                # flag=False
                # break
                return False

    return len(l)==0
    #return len(l) == 0 and flag


print(is_paranthesis_matched("((((())))))"))
