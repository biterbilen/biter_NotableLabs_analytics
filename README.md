# biter_NotableLabs_analytics
ML for flow cytometry

# HOWTO 
1. Download live_dead_debris folder from Notable Labs into data directory
2. Run bin/flow/main.ipynb

# CONCLUSION 
Default initialization of 3-component-GMM didn't work well for this task

## TODO 
1. initialize cluster centers with k-means 
2. increase the number of components and use information gain to assign clusters to the known labels
3. Compare it to GBMs 
