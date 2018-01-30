import numpy as np
import hypertools as hyp
import seaborn as sns

x = hyp.load('mushrooms')

def data_manip(x, offset):
    return np.subtract(hyp.tools.format_data(x), offset)

y = data_manip(x, 3)
sns.heatmap(y)
