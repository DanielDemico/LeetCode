class Solution(object):
    def buildArray(self, target, n):
        i_stack = []
        s_stack = []
        
        idx_c = 0
        for i in range(n+1):
            if i>0:
                if i_stack == target:
                    return s_stack

                i_stack.append(i)
                s_stack.append("Push")
                if i_stack[-1] != target[idx_c]:
                    i_stack.pop()
                    s_stack.append("Pop")
                else:
                    idx_c +=1
        return s_stack
            