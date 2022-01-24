import numpy as np

def change_toarray(list_values):
    if type(list_values) == list:
        return np.asarray(list)
    else:
        return 'The input is NOT a list'
