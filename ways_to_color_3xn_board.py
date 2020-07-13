'''
We can use either a combination of 3 colors
or 2 colors.choosing 3 colors out of 
4 is 4C3 and arranging them 
in 3! ways,  choosing 2 colors out 
of 4 is 4C2 and while arranging
we only choose which of them could be at 
centre, that would be 2! ways. 
Answer = 4C3*3! + 4C2*2! = 36


the ways in which colors are going to be filled depends just upon
the color pattern in the current column.Since we can only have a
combination of two colors and three colors in a column so for a  particular 2 color arrangement
we get 7 valid arrangements for 2 color and 10 for 3 color and for particular 3 color arrangement
we get 5 valid arrangements for 2 color and 11 for 3 color
'''
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        comb_using_3_color=24 #4C3
        comb_using_2_color=12 #4C2
        
        for i in range(2,A+1):
            t=comb_using_3_color
            comb_using_3_color=(11*comb_using_3_color+10*comb_using_2_color)%1000000007
            comb_using_2_color=(5*t+7*comb_using_2_color)%1000000007
        result=(comb_using_3_color+comb_using_2_color)%1000000007
        return result
