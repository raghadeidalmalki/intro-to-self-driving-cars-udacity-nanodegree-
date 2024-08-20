import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I
    
##for the matrix multiplication __mul__ 
def dot_product(vector_one, vector_two): 
    result = 0 
    for i in range(len(vector_one)): 
        result += vector_one[i] * vector_two[i] 
        
    return result

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.h == 1:  # for a 1x1 matrix
            return self[0][0]
        elif self.h == 2:  # for a 2x2 matrix
            return self[0][0] * self[1][1] - self[0][1] * self[1][0]

        
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        trace_sum = 0
        for i in range(self.h):
            trace_sum += self[i][i]
        return trace_sum

        
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        
        matrix_inverse = []
        
        determ = self.determinant()
        
        if self.h == 1:
            matrix_inverse = [[1/determ]]
            
        elif self.h == 2:  # for a 2x2 matrix
            a, b = self[0][0], self[0][1]
            c, d = self[1][0], self[1][1]
            determinant = a * d - b * c 
            
            matrix_inverse = [
                [d / determ, -b / determ], 
                [-c / determ, a / determ]
            ]
        
        return Matrix(matrix_inverse)
        

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here

        matrix_transpose = []
        for i in range(self.w):
            row = []
            for j in range(self.h):
                row.append(self[j][i])
            matrix_transpose.append(row)
        return Matrix(matrix_transpose)
    
    

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        
        matrixSum = []
    
        # matrix to hold a row for appending sums of each element
        row = []
    
        # For loop within a for loop to iterate over the matrices
        for i in range(self.h):
            row = [] # reset the list
            for j in range(self.w):
                row.append(self[i][j] + other[i][j]) # add the matrices
            matrixSum.append(row)
        return Matrix(matrixSum)


        #

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        neg_matrix = []
        for i in range(self.h):
            #create an empty list row=[]
            row=[]
            for j in range(self.w):
                row.append(-self[i][j]) # 
            neg_matrix.append(row)
        return Matrix(neg_matrix)
    
    
        #

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        sub_value = []
        for i in range(self.h):
            #create an empty list row=[]
            row = []
            for j in range(self.w):
                row.append(self[i][j] - other[i][j])
            sub_value.append(row)
        
        return Matrix(sub_value)
    
        #
        



    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        
        multiply = []

        other_T = other.T()
    
        for i in range(self.h):
            row = []
            for j in range(other_T.h):
                row.append(dot_product(self.g[i],other_T.g[j]))
            multiply.append(row)
                
        return Matrix(multiply)
    
        #

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            output_matrix = []
            for i in range(self.h):
                row = []
                for j in range(self.w):
                    row.append(other*self[i][j])
                output_matrix.append(row)
            return Matrix(output_matrix)
            #
            