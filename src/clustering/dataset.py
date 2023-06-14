'''
I have provided a list of names of psychoactive substances from 
https://en.wikipedia.org/wiki/List_of_psychedelic_drugs as a dataset for this project.

Naturally, this program can run on any list of names of drugs, but I have provided this list for testing purposes.

'''

import pubchempy as pcp



def get_smiles(file_name):
    with open(file_name,"r+",encoding="utf8") as f:
        for row in f.read().split("\n"):
            try:
                results = pcp.get_compounds(row, 'name')
                for res in results:
                    data.append([row,res.canonical_smiles])
                    # List all possible properties stored in the object
                    print(dir(res))
                    exit()
            except Exception as e:
                print(f"Error {e}")
    return data

def store_smiles(data_file,data):
    with open(data_file,"w+",encoding="utf8") as f:
        f.write(str(data))


def remove_duplicates(data):
    return list(set(data))


if __name__ == "__main__":
    data = []
    data_folder = r"C:\Users\0xdan\Documents\CS\Catergories\Healthcare_Medical\Drug Discovery\DrugInteractions\data"
    names = f"{data_folder}\drugs.txt"
    data = get_smiles(names)
    store_smiles(fr"{data_folder}\smiles.txt",data)
