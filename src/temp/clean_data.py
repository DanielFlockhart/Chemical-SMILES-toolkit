import os
import sys
import ast
sys.path.insert(0, os.path.abspath('..'))
from utils import *

# Iterate through clustered data in the form [cluster1,cluster2,cluster3...]
# Where Cluster = [[name of chemical,smile],[name of chemical,smile]...]
# Iterate through and remove any duplicate chemicals based on their names.

data_folder = os.path.join(get_directory(),"data")
data_file = os.path.join(data_folder,"smiles.txt")
data = []
# Read in data
with open(data_file,"r") as f:
    data = ast.literal_eval(f.read())

# Iterate through data
for i,cluster in enumerate(data):
    # Iterate through cluster
    for j,chemical in enumerate(cluster):
        # Get name of chemical
        name = chemical[0]

        # Iterate through cluster again
        for k,chemical2 in enumerate(cluster):
            # Get name of chemical
            name2 = chemical2[0]

            # Check if names are the same
            if name == name2 and j != k:
                # Remove chemical from cluster
                cluster.pop(k)

    # Replace cluster with new cluster
    data[i] = cluster

# # Write data to file
with open(data_file,"w") as f:
    f.write(str(data))
