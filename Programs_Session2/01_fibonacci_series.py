# import functions and libraries of your choice
import numpy as np
import matplotlib.pyplot as plt

# ask for user input
n = int(input("Enter the number of terms in the series:"))

# create a static array to store the sequence values
f = np.zeros(n, dtype=np.int16)

# Usual method
# f[1] = 1
# for i in range(2, n+1):
#     f[i] = f[i-1] + f[i-2]

# A Pythonic implementation
a = 0
b = 1
for i in range(1, n):
    a, b = b, a+b # Swap and Unpack
    f[i] = a

# Print them out
print("The fibonacci series upto {} term(s) is(are):".format(n), f)

plt.figure()
plt.plot(f, color='r', marker='*', label='fibonacci numbers')
plt.grid()
plt.legend()
plt.title('Fibonacci numbers upto {} terms'.format(n))
plt.savefig('images/fib_numbers.png', format='png', dpi=400, bbox_toinches='tight')
plt.show()
