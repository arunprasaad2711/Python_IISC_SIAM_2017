rm *~ *.so *.o
f2py -m matmul1 -c matmul1.f90
mv *.so matmul1.so
