import numpy as np
import matplotlib.pyplot as plt
import hypertools as hyp
from examples.helpers import add_it

print('Hello, CDL!')  # Python 3.x doesn't support
print('Hope you like the tutorial ')  # Python 3.x does support this!

# example for loop for debugging

for i in range(5):
    print('i = ', i) # this formatting will fail with Python 3.x

    # walk through add_it function in separate script
    print(f'i + 4 = {add_it(i)}') # this formatting will fail with Python 3.x

# example for plot debugging

locs = np.array([[-61., -77., -3.],
                 [-41., -77., -23.],
                 [-21., -97., 17.],
                 [-21., -37., 77.],
                 [-21., 63., -3.],
                 [-1., -37., 37.],
                 [-1., 23., 17.],
                 [19., -57., -23.],
                 [19., 23., -3.],
                 [39., -57., 17.],
                 [39., 3., 37.],
                 [59., -17., 17.]])

# plot them

plt.plot(locs)

# plot them with hypertools!

hyp.plot(locs, '.')

# it even catches typos!
print('Thats all folks')

print("That's all folks")