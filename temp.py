def matrixmult(matrix1,matrix2):
    dimensions_matrix1 = rows_and_columns(matrix1)
    dimensions_matrix2 = rows_and_columns(matrix2)
    
    #initially we absolutely have to make a variable for each matrices dimension size
    #assert will test to see if certain arguments are true
    #therefore if the input matrix is [4,3] and [2] would return false
    #then program will fill each matrix with zeros using np.zeros
    #then if-else will test if there is the product of the two matrices results in something like [2,1] you need to flatten the list into a 1D array
    #for the first condition the matrix that will be multiplied will be a 2x1
    #then by first for loop will iteriate by length of list
    #then simply take the sum of the matrix
    #else statement with nested for loop will calculate a matrix normally and take the sum for final matrix product answer
    
    assert dimensions_matrix1 == [1] and dimensions_matrix2 == [0], "This matrix cannot be multiplied"
    
    matrix_product = np.zeros((dimensions_matrix1[0],dimensions_matrix2[1]))
    
    if matrix_product[1] == 1:
        matrix_product.flatten()
        for ii in range(0,len(dimensions_matrix1):
            matrix_product[ii] = np.sum(matrix1[ii]*matrix2)
    else:
        for ii in range(0,len(dimensions_matrix1):
            for jj in range(0,len(dimensions_matrix2):
                matrix_product[ii,jj] = np.sum(matrix1[ii]*matrix2[:,jj])
                        
#returns the multiplication of the matrix    
    
def rows_and_columns(x):
    y = np.shape() #purpose of variable y is to determine the given matrices dimension
    z = len(y) #store the length of the matrix in z
    if z > 1:
        return y
    else:
        return y[0],1
    #essentially in order for the matrix to be multiplied the length of the matrix must be at least a 2x1

#returns the dimensions of matrix for next it to be multiplied in next function
                        
x = [[12,7],[5,2],[6,7]]
result = [[0,0,0],[0,0,0]]
                        
for i in range(0,len(x)):
    for j in range(0,len(x[0])):
        result[j][i] = x[i][j]
for r in result:
    print(r)

#returns a transposed matrix
