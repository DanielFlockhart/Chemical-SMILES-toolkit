'''
I have provided a list of names of psychoactive substances from 
https://en.wikipedia.org/wiki/List_of_psychedelic_drugs as a dataset for this project.

Naturally, this program can run on any list of names of drugs, but I have provided this list for testing purposes.

'''

import pubchempy as pcp
import os
import sys
import ast
sys.path.insert(0, os.path.abspath('..'))
from utils import *

class Dataset:
    def __init__(self):
        self.data = []
        self.data_folder = os.path.join(get_directory(),"data")
        self.names = os.path.join(self.data_folder,"drugs.txt")
        self.smiles = os.path.join(self.data_folder,"smiles.txt")

    def get_smiles(self):
        """
        For Each Chemical in the List of Chemicals, Get The Canonical SMILES and Store It In A List
        """
        with open(self.names,"r+",encoding="utf8") as f:
            data = ast.literal_eval(f.read())
            for x in range(len(data)):
                try:
                    results = pcp.get_compounds(data[x], 'name')
                    for res in results:
                        self.data.append([data[x],res.canonical_smiles])
                except Exception as e:
                    print(f"Error {e}")

    def store_smiles(self):
        """
        Store The Canonical SMILES In A Text File
        """
        with open(self.smiles,"w+",encoding="utf8") as f:
            f.write(str(self.data))


    def clean_data(data):
        """
        Unused Function But Kept For Future Reference
        """
        return list(set(data))
