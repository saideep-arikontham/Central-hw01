#!/usr/bin/env python
# coding: utf-8

# In[114]:


import matplotlib.pyplot as plt
import numpy as np
from readit import create_pseudo_random_uniform_data


figure, axis = plt.subplots(1, 3,figsize=(20,5))
sample_size = 20 

#plotting standard error of 10 samples

N = 10  
data = create_pseudo_random_uniform_data(0.0, 1.0, (N, sample_size))
sample_sizes = [i for i in range(1,sample_size+1)]
standard_errors = np.std(data,axis=0) / np.sqrt(sample_sizes)

axis[0].plot(standard_errors)
axis[0].set_title("10 samples")
axis[0].set_xticks([5,10,15])

#plotting standard error of 100 samples

N = 100  
data = create_pseudo_random_uniform_data(0.0, 1.0, (N, sample_size))
sample_sizes = [i for i in range(1,sample_size+1)]
standard_errors = np.std(data,axis=0) / np.sqrt(sample_sizes)

axis[1].plot(standard_errors)
axis[1].set_title("100 samples")
axis[1].set_xticks([5,10,15])

#plotting standard error of 1000 samples

N = 1000  
data = create_pseudo_random_uniform_data(0.0, 1.0, (N, sample_size))
sample_sizes = [i for i in range(1,sample_size+1)]
standard_errors = np.std(data,axis=0) / np.sqrt(sample_sizes)

axis[2].plot(standard_errors)
axis[2].set_title("1000 samples")
axis[2].set_xticks([5,10,15])

plt.savefig("figs/std_err.png")
plt.show()
