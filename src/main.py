from clustering import cluster as cl
from clustering import evaluation as ev
from clustering import dataset as ds


'''
User inputs a smile and the program will return a cluster of similar smiles and their names

Current Functionality:

Functionality to add:

'''


# Get data
# cluster
# evaluate
# get Cluster




def evaluate_cluster_counts(min_clusters,max_clusters):
    pass

def cluster(n_clusters):
    cl.cluster(n_clusters)


def main(folder):
    
    # Get the smile from the user
    smile = input("Enter a smile: ")
    # Get the similar smiles
    similar_smiles = cl.get_similar_smiles(smile,folder)
    # Print the similar smiles
    # print(similar_smiles)
    # Get the longest name out of the array of similar smiles names
    longest_name = max([len(item[0]) for item in similar_smiles])

    # Print the names of the similar smiles and their smiles
    for item in similar_smiles:
        # Normalise the start point of the smiles
        gap = (longest_name - len(item[0])) * " "

        # Print the names red and the smiles green
        print(f"\033[91m{item[0]}\033[00m{gap} \033[92m{item[1]}\033[00m")
        
        

test_smile = "CCN(CC)C(=O)C1CN(C2CC3=C(NC4=CC=CC(=C34)C2=C1)Br)C"
if __name__ == "__main__":
    main(r"C:\Users\0xdan\Documents\CS\Catergories\Healthcare_Medical\Drug Discovery\DrugInteractions\data")