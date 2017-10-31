# Demonstration of Data Files using *.mat files and *.npy, *.npz files

import numpy as np
import scipy.io as sio

# -----------------------------------
## Part 0 - Generation of random data
# -----------------------------------

x = [[1, 2, 3], [4.0, 5, 6], [7, 8, 9]]
np_x = np.array(x) + 4.0
np_y = 5.0*np_x

# -----------------------------------
## Part 1 - Usage of *.mat files
# -----------------------------------

# Creation of a dictionary for mat file

data_mat = {}

# File name for the mat file
mat_fname = 'data_arrays.mat'

# Adding data to the dictionary

data_mat['x'] = x
data_mat['np_x'] = np_x
data_mat['np_y'] = np_y

# for key in data_mat:
#    print(key, data_mat[key], type(data_mat[key]))

# Saving the dictionary

sio.savemat(mat_fname, data_mat)

# Open a the saved mat file using a new dictionary
new_data_mat = sio.loadmat(mat_fname)

# for key in new_data_mat:
#    print(key, new_data_mat[key], type(new_data_mat[key]))

# -----------------------------------
## Part 2 - Usage of *.npy files
# -----------------------------------

# Storing the data in *.npy files
np.save('array_x', x)
np.save('np_array_x', np_x)
np.save('np_array_y', np_y)

# Opening the data in *.npy files
new_x = np.load('array_x.npy')
new_npx = np.load('np_array_x.npy')
new_npy = np.load('np_array_y.npy')

# print(new_x)
# print(new_npx)
# print(new_npy)

# -----------------------------------
## Part 3 - Usage of *.npz files
# -----------------------------------

# Storing the data in *.npz files
np.savez('npz_demo', x=x, np_x=np_x, np_y=np_y)

# Opening the data in *.npz files
new_npz_dict = np.load('npz_demo.npz')

for key in new_npz_dict:
    print(key, new_npz_dict[key], type(new_npz_dict[key]))





