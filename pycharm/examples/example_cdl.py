import hypertools as hyp
import supereeg as se
import matplotlib
matplotlib.use("Agg")

# load example data
bo = se.load('example_data')

hyp.plot(bo.data.head())
# check out the brain object (bo)
bo.info()

# look data, stored as pandas dataframe
bo.data.head()

# then can visualize locations
bo.plot_locs()

# visualize the data with plot_data
# the default time window is the first 10 seconds, but you can specify your own timewindow
bo.plot_data(time_min=0, time_max=5)