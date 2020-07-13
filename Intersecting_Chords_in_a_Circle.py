### CATALAN NUMBER SERIES ###


class Solution:
    # @param A : integer
    # @return an integer
    def chordCnt(self, A):
        catalan=[0]*(A+1)
        catalan[0]=1
        catalan[1]=1
        for i in range(2,A+1):
            catalan[i]=0
            for j in range(i):
                catalan[i]+=catalan[j]*catalan[i-j-1]
        return (catalan[A])%1000000007
