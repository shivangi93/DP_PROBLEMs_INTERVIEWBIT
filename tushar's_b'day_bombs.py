##### Since we need to find the maximum number of kick hits so we will choose that friend whose kick strength is minimum and less than or equal to resistance power of Tushar ######

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        minvalue,minindex=min((v,i) for (i,v) in enumerate(B))       ### finding the minimum kick strength and its index ###
        result=[minindex]*(A//minvalue)                             ### storing the minimum value's index in the result list ###
        i=0
        diff=A%minvalue
        ### if difference is zero then return the result list ###
        if diff==0:
            return result
        k=0
        i=0
        ### if difference is not zero then we need to check other combinations that can be replaced with the minimum value without changing the length of the result and whose index
        is lesser than the minimum index as we need lexicographically smallest order of friends to kick Tushar ###
        
        while diff>0 and i<minindex and k<len(result):
            if B[i]-minvalue<=diff:
                result[k]=i
                k+=1
                diff-=(B[i]-minvalue)
            else:
                i+=1
        return result
