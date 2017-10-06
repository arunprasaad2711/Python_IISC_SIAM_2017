rm *~ *.so *.c
echo "Running in Python 3"
python setup.py build_ext --inplace

# use this to see how your cython code can be optimized
cython -a matmul_cython.pyx
