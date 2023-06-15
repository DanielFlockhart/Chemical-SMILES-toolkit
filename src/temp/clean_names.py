import os
import sys
import ast
sys.path.insert(0, os.path.abspath('..'))
from utils import *

# Iterate through clustered data in the form [cluster1,cluster2,cluster3...]
# Where Cluster = [[name of chemical,smile],[name of chemical,smile]...]
# Iterate through and remove any duplicate chemicals based on their names.

data_folder = os.path.join(get_directory(),"data")
data_file = os.path.join(data_folder,"drugs.txt")
with open(data_file,"r") as f:
    data = f.read().split("\n")

# Iterate through data
for i,drug1 in enumerate(data):
    for j, drug2 in enumerate(data):
        if i!=j and drug1 == drug2:
            data.pop(j)

# # Write data to file
with open(data_file,"w") as f:
    f.write(str(data))
