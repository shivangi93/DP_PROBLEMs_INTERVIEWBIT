### we need to solve for subproblems.conside an example:A="kill" and B=['k','il','l']
### so we will check for 'k' and wordbreak('ill') then 'ki' and wordbreak('ll')
### then 'kil' and wordbreak('l') then 'kill' and wordbreak(' ').since there is redundancy so we use dp here.

class Solution:
    # @param A : string
    # @param B : list of strings
    # @return an integer
    def wordBreak(self, A, B):
        dp=[0]*(len(A)+1)
        dp[0]=1 ## base case
    
        for i in range(len(A)):
            for j in B:
                if A[i+1-len(j):i+1]==j and dp[i+1-len(j)]==1 :
                    dp[i+1]=1
                    break
        return dp[len(A)]
