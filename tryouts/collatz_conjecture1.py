import matplotlib.pyplot as plt

def if_odd(num):

    if(num % 2 == 1):
        return True
    else:
        return False
        
def conjecture(num):

    i = 0
    temp = num
    seq = [num]
    
    while(temp != 1):
        
        if(if_odd(temp)):
            temp = 3*temp + 1
        else:
            temp = temp // 2  # // means integer division
        
        i += 1
        seq.append(temp)
    
    return i, seq

In1 = int(input("Enter a number for analysis:"))

iter1, sequences1 = conjecture(In1)

# Opens up an empty canvas
plt.figure()
plt.plot(sequences1, color='r', marker='*', \
    label='Num = {}, Iterations = {}'.format(In1, iter1))
plt.title("Collatz Conjecture Example")
plt.grid()
plt.legend()
plt.savefig("conjecture1.png", format='png', dpi=400)
plt.show()

# % matplotlib qt5





