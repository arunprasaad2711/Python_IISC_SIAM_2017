import numpy as np
import matplotlib.pyplot as plt

n = int(input("Enter the number of terms:"))

f = np.zeros(n, dtype=np.int16)

a = 0
b = 1

for i in range(1, n):
    a, b = b, a+b # swap and unpack
    f[i] = a

print("The fibonacci series upto {} term(s) is(are):".format(n), f)

plt.figure()
plt.plot(f, color='r', marker='*', label='fibonacci numbers')
plt.grid()
plt.legend()
plt.title('Fibonacci numbers upto {} terms'.format(n))
plt.savefig('fib_numbers.png', format='png', dpi=400, bbox_toinches='tight')
plt.show()
