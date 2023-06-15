from rdkit import Chem
from rdkit.Chem import Draw

def generate_canonical_smile():
    smile = "C1=CC=CC=C1"
    molecule = Chem.MolFromSmiles(smile)
    
    if molecule is not None:
        Draw.MolToFile(molecule, "canonical_smile.png")

generate_canonical_smile()
# Given a canonicle smile, a 2D structure can be generated using the rdkit library.

class Structure:
    def __init__(self,smile):
        self.smile = smile
    
    def build_structure(self):
        """
        Builds a 2D structure from a smile
        """
        m = Chem.MolFromSmiles(self.smile)
        return m