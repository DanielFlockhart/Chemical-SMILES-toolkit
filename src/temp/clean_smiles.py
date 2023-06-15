import os
import sys
import ast
sys.path.insert(0, os.path.abspath('..'))
from utils import *

# Iterate through clustered data in the form [[name of chemical,smile],[name of chemical,smile]...]
# Iterate through and remove any duplicate chemicals based on their names.

data_folder = os.path.join(get_directory(),"data")
data_file = os.path.join(data_folder,"smiles.txt")
data = []
# Read in data
with open(data_file,"r") as f:
    data = ast.literal_eval(f.read())

# Iterate through data
for i,chemical in enumerate(data):
    for k,chemical2 in enumerate(data):
        # Get name of chemical
        name = chemical[0]

        # Get name of chemical
        name2 = chemical2[0]

        # Check if names are the same
        if name == name2 and i != k:
            # Remove chemical from cluster
            data.pop(k)
    

# # Write data to file
with open(data_file,"w") as f:
    f.write(str(data))
