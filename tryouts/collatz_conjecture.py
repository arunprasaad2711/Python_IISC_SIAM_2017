#   Program to test the collatz conjecture for positive integers
# 
#   Collatz Conjecture: 
#       A statement from Lothar Collatz, also called as 3n+1 problem. (Has several names)
#
#       * If a positive interger is even, divide it by 2.
#       * If it is odd, then multiply by 3 and add 1 to make it even
#
#       Repeat steps 1 and 2 recursively. Usually, a positive integer converges to 1.
#
#       Does this procedure applies true to *all* integers - open problem!

from matplotlib import pyplot as plt

def odd(number):

    if(number%2 == 1):
        return True
    else:
        return False

def collatz(num_in):

    i = 0
    temp = num_in
    seq = [num_in]
    
    while(temp != 1):
    
        if(odd(temp)):
            temp = 3*temp + 1
        else:
            temp = temp // 2
            
        seq.append(temp)
        i += 1

    return i, seq    

In1 = int(input("Enter positive integer 1 for the test:"))
# In2 = int(input("Enter positive integer 2 for the test:"))
# In3 = int(input("Enter positive integer 3 for the test:"))
# In4 = int(input("Enter positive integer 4 for the test:"))

iters1, sequence1 = collatz(In1)
# iters2, sequence2 = collatz(In2)
# iters3, sequence3 = collatz(In3)
# iters4, sequence4 = collatz(In4)

print(sequence1)

plt.figure()
plt.plot(sequence1, color='r', marker='*', label='Num = {}, Iters = {}'.format(In1, iters1))
# plt.plot(sequence2, color='b', marker='*', label=str(In2))
# plt.plot(sequence3, color='g', marker='*', label=str(In3))
# plt.plot(sequence4, color='k', marker='*', label=str(In4))
plt.grid()
plt.title("Collatz Conjecture Sequence Evolution for some input numbers")
plt.legend()
plt.savefig("conjecture.png", format='png', dpi=400, bbox_toinches='tight')
plt.show()


