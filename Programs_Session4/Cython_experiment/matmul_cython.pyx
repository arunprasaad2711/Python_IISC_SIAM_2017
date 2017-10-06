
#Cython - C + Python

#Write Python code with some additional constraints of C to make the Python Code run at speeds comparable with C Programs.

#Unlike other options that require one to know C/C++/Fortran, you do not need that!

#Speed is obtained by 
#    * converting the variables from dynamic (data type changeable throughout the program) to static (data type constant throughout the program) by specifying typing info. (This skips the data check requirement that is done *everytime* the variable is accessed)

#Needs a C compiler! - GCC

#Data definitions:
#    def     Function or variable definition only in Python. Only Python can call them
#    cdef    Function or variable definition only in C. Only Cython can call them inside Python.
#    cpdef   Function or variable definition in C and Python. Python builds a "wrapper" code to call the C function/variable.
#            Some features accessible in cdef are not possible in cpdef. Otherwise, can be used almost all the time!


cimport numpy as np
# cpimport numpy as np # did not work

# since this function is defined with "cpdef", both Python and C can call it!
# if it is defined with "def", only Python can call it.
# if it is defined with "cdef", only C can call it. So, when you import this module and call it in C, Python would not be able to call it!

cpdef matmul1(np.ndarray[double, ndim=2] mat1, np.ndarray[double, ndim=2] mat2, np.ndarray[double, ndim=2] r):
    
    # Variables can be defined with cdef or cpdef as they are not required by Python directly!
    cpdef unsigned int i, j, k, r1, r2, c2
    
    r1 = mat1.shape[0]
    r2 = mat2.shape[0]
    c2 = mat2.shape[1]
    
    # r[:,:] = 0.0
    
    for i in range(0, r1):
        for j in range(0, c2):
            r[i,j] = 0.0
            # r[i][j] = 0.0
            for k in range(0, r2):
                # r[i,j] += mat1[i,k]*mat2[k,j]
                r[i,j] = r[i,j] + mat1[i,k]*mat2[k,j]
    
        
