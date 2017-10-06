'''
Numerical Integration Library

Contains functions for numerical integration
'''

import numpy as np

class rk_schemes:

    def rk4(inp_func, init_conditions, t, args):

        nt = len(t)
        n_outs = len(init_conditions)
        
        # print("init_conditions = ", init_conditions)
        
        states = np.zeros((nt, n_outs))
        k1 = np.zeros((nt, n_outs))
        k2 = np.zeros((nt, n_outs))
        k3 = np.zeros((nt, n_outs))
        k4 = np.zeros((nt, n_outs))
        
        dt = t[1] - t[0]
        
        states[0,:] = init_conditions
        
        for i in range(1, nt):
            var_ins = states[i-1,:]
            k1[i-1,:] = inp_func(var_ins, t[i], *args)
            k2[i-1,:] = inp_func(var_ins+k1[i-1,:]*dt*0.5, t[i], *args)
            k3[i-1,:] = inp_func(var_ins+k2[i-1,:]*dt*0.5, t[i], *args)
            k4[i-1,:] = inp_func(var_ins+k3[i-1,:]*dt, t[i], *args)
            
            states[i,:] = var_ins + (k1[i-1,:] + 2.0*k2[i-1,:] + 2.0*k3[i-1,:] + k4[i-1,:])*dt/6.0
            # print(i, states[i,:])

        return states
