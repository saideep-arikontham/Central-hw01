import numpy as np

def create_pseudo_random_uniform_data(low,high,size):
    '''
    function to create random uniform distribution in [0,1) (default range) of specified size.
    Pass the lower bound, upper bound and size of the array.
    Returns ndarray
    '''
    data = np.random.uniform(low=low,high=high,size=size)
    return data