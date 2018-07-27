from helpers import exp_it

# example for loop for profiling

try_fl = []
for i in range(50000):
    try_fl.append(exp_it(i))

# example list comprehension for profiling

try_lc = [exp_it(i) for i in range(50000)]
