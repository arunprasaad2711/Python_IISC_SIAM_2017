import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt
from PIL import Image

fname='images/stinkbug.png'

image = Image.open(fname).convert("L")
input_mat = np.asarray(image)

rows, columns = np.shape(input_mat)
print(rows, columns)

cmap = 'gray'

# rows, columns = 8, 10

filt_mat1 = np.zeros((rows, columns))
filt_mat2 = np.zeros((rows, columns))

laplace_mat1 = np.array([[ 0.0, -1.0,  0.0], [-1.0, 4.0, -1.0], [ 0.0, -1.0,  0.0]])
laplace_mat2 = np.array([[-1.0, -1.0, -1.0], [-1.0, 8.0, -1.0], [-1.0, -1.0, -1.0]])

for i in range(1, rows-1):
    for j in range(1, columns-1):
        temp_mat = input_mat[i-1:i+2, j-1:j+2]
        filt_mat1[i,j] = np.sum(temp_mat*laplace_mat1)
        filt_mat2[i,j] = np.sum(temp_mat*laplace_mat2)
            
plt.figure(figsize=(15,10))

plt.subplot(131)
plt.imshow(input_mat, cmap=cmap, interpolation='nearest')
plt.axis('off')
plt.title('Original Image in grey scale')

plt.subplot(132)
plt.imshow(filt_mat1, cmap=cmap, interpolation='nearest')
plt.axis('off')
plt.title('Filtered Image using L4 filter')

plt.subplot(133)
plt.imshow(filt_mat2, cmap=cmap, interpolation='nearest')
plt.axis('off')
plt.title('Filtered Image using L8 filter')
plt.show()

