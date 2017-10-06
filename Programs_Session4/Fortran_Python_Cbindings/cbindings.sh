gfortran -O3 -funroll-loops -ffast-math -floop-strip-mine -shared -fPIC \
         -o matops1.so matops.f90
echo "Running in Python 3"
