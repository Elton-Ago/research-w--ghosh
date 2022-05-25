import numpy as np

def matmult(matrix1,matrix2):
    matrix1 = np.array[1,2,3,4]
    matrix2 = np.array[5,6,7,8]

    a0 = np.array((matrix1[:1])*(matrix2[:1])+((matrix1[1:2])*(matrix2[2:3])))
    a1 = np.array((matrix1[:1])*(matrix2[1:2])+((matrix1[1:2])*(matrix2[3:4])))
    a2 = np.array((matrix1[2:3])*(matrix2[:1])+((matrix1[-1:])*(matrix2[-2:-1])))
    a3 = np.array((matrix1[-2:-1])*(matrix2[1:2])+((matrix1[:-1])*(matrix2[:-1])))

    return(a0)
    return(a1)
    return(a2)
    return(a3)

matmult()

a = [1,2,3,4,3,2,2,1,3]
b = [1,4,6,6,4,1,9,7,8]

cc = np.zeros(np.shape())
nn = cc

for ii in range(0,len(nn):
        for jj in range(0,len(nn):
            np.sum(a[:ii],a[:,jj])

