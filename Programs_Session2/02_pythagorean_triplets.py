import numpy as np
import matplotlib.pyplot as plt

N = 3

triples = np.zeros((3, 2*N+1, 2*N+1), dtype=np.int64)

for i in range(-N, N+1):
    for j in range(-N, N+1):
        triples[:, i, j] = i*i - j*j, 2*i*j, i*i + j*j
        # print(triples[:, i, j])

bases = triples[0,:,:].flatten()
heights = triples[1,:,:].flatten()
hypotenuses = triples[2,:,:].flatten()

# print(len(bases))

xnumbers = np.arange(np.min(bases), np.max(bases)+1, 1)
ynumbers = np.arange(np.min(heights), np.max(heights)+1, 2)

plt.figure(figsize=(15,10))
plt.scatter(bases, heights, color='r', s=20, label='triples')
# plt.xticks(xnumbers)
# plt.yticks(ynumbers)
plt.title('Maximum of {} Pythagorean Triplets from the Origin in all directions'.format(N))
plt.legend()
plt.grid()

# for i in range(0, len(bases)):
#     plt.plot((0,bases[i]), (0,heights[i]), color='k')

plt.savefig('images/pythagorean_triples.png', format='png', dpi=400, bbox_toinches='tight')
plt.show()
