from rdkit import Chem
from rdkit.Chem import Draw
from PIL import Image

import pubchempy as pcp
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
from utils import *

# Given a canonicle smile, a 2D structure can be generated using the rdkit library.

class Structure:
    def __init__(self,smile):
        self.smile = smile
        self.molecule = self.build_structure()
        self.name = self.get_name()
        self.data_folder = os.path.join(get_directory(),"data")
        self.structures = os.path.join(self.data_folder,"2D-Structures")
        
    
    def build_structure(self):
        """
        Builds a 2D structure from a smile
        """
        m = Chem.MolFromSmiles(self.smile)
        return m
    
    def save_structure(self):
        """
        Saves the 2D structure as a png to the data folder
        """
        if self.molecule is not None:
            Draw.MolToFile(self.molecule, self.structures+fr"\{self.name}.png")

    def get_name(self):
        """
         Gets the name of the chemical from the smile
        """
        results = pcp.get_compounds(self.smile, 'smiles')

        return results[0].synonyms[0]

    def display_structure(self):
        """
        Displays the 2D structure using PIL
        """
        img = Image.open(self.structures+fr"\{self.name}.png")
        img.show()