class Solution:
	# @param A : list of list of integers
	# @return an integer
	def solve(self, A):
	   
	    row=len(A)
	    column=len(A[0])
	#### creating Matrix that contains the count of consecutive number of 1s columnwise ####
        for j in range(column):
            count = 0
            for i in range(row):
                if A[i][j]==1:
                    count = count + 1       # Number of 1s in row
                else:
                    count = 0               # If 0 then count=0
                A[i][j] = count             # Setting Matrix entry with the count of 1s
        for i in range(row):
            A[i].sort(reverse=True)         # Descending order arrangement of 1s count
        max_area = 0
        for i in range(row-1, -1, -1):
            for j in range(column-1, -1, -1):
                
                max_area = max(max_area, A[i][j] * (j + 1)) # Maximum area by finding length*breadth
        return max_area # max_area denotes the Maximum area of the rectangle with 1s
	           
