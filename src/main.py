from clustering import cluster as cl
from clustering import evaluation as ev
from clustering import dataset as ds

from visualisation import structure_builder as sb
from utils import *
import os
'''

Current Functionality:
    - Allows user to use a list of names of drugs from a text file to create a list of smiles and store them in a text file
    - Allows user to cluster the smiles and store the clustered data in a text file
    - Allows user to input a smile and get a list of similar smiles and their names
    - Allows user to input a smile and get a 2D structure of the chemical
    - Allows user to input a smile and get the name of the chemical

Functionality to add:

'''

def cluster_different_dataset():
    '''
    Re-Cluster the data using a different dataset user has provided in drugs.txt
    
    '''
    linebreak()
    print('''
    Please note that this will overwrite the current clustered data.

    Please make sure that the data file is in the format of a list of names of drugs seperated by new lines and is in \Chemical-SMILES-toolkit\data\drugs.txt.
    Example of drugs.txt:
    drug1
    drug2
    drug3
    ...

    
    ''')
    # Ask user for confirmation
    if confirmation():
        linebreak()
    else:
        return
    print("Loading new dataset into smiles.txt, this may take some time depending on how many drugs are in the dataset")
    
    # Loads new dataset
    dataset = ds.Dataset()

    # Get the smiles for each chemical from database
    dataset.get_smiles()

    # Remove duplicates
    #dataset.clean_data()

    # Store the smiles with their corresponding name in a text file
    dataset.store_smiles()
    print("New Data stored in smiles.txt")

    # Cluster the data
    cluster()

def cluster():
    '''
    Uses Agglomerative Clustering with Complete Linkage to cluster the data
    Distance matrix is calculated using the Levenshtein distance

    '''
    linebreak()

    # Get the number of clusters from the user
    n_clusters = get_cluster_input()

    new_cluster = cl.Cluster(n_clusters)
    new_cluster.cluster()


def get_related_chemicals():
    """
    Get the similar smiles to a given smile
    """
    linebreak()
    
    print('''
    By Default the program will use the clustered data from the Github repository of Pychoactive substances as mentioned Previously
    ''')
    # Get the smile from the user
    smile = input("Enter a smile: ")

    cluster = cl.Cluster()
    

    # Get the similar smiles
    similar_smiles = cluster.get_similar_smiles(smile)
    

    # Get the longest name out of the array of similar smiles names
    longest_name = max([len(item[0]) for item in similar_smiles])

    # Print the names of the similar smiles and their smiles
    for item in similar_smiles:
        # Normalise the start point of the smiles
        gap = (longest_name - len(item[0])) * " "

        # Print the names red and the smiles green
        print(f"\033[91m{item[0]}\033[00m{gap}{colour_smile(item[1])}")

        
def smile_to_2D_structure():
    """
    Converts a smile to a 2D structure and displays it
    """

    # Get the smile from the user
    smile = input("Enter a smile: ")

    chem = sb.Structure(smile)
    chem.save_structure()
    chem.display_structure()

def get_name_from_smile():
    """
    Gets the name of a chemical from a smile
    """

    # Get the smile from the user
    smile = input("Enter a smile: ")
    chem = sb.Structure(smile)
    print("The SMILE corresponds to the chemical -> " + chem.get_name())


def main():
    print(("-"*10)+" Welcome chemical SMILES toolkit "+("-"*10))
    print('''
    The Github repository comes with a pre-clustered dataset of 1411 Psychoactive Substances with 100 clusters as an example.
    Feel free to use this dataset or cluster your own dataset.
    Please choose from the follow options to continue:
    
    1. Get similar SMILE to a given SMILE with current clusters
    2. Re-cluster data with a different number of clusters
    3. Re-cluster data with a different dataset
    4. Convert a SMILE to a 2D structure and display it
    5. Get the name of a chemical from a SMILE

    ''')
    choices = 5
    choice = -1
    while choice < 1:
        try:
            choice = int(input(f"Selection : "))
            if choice > choices or choice < 1:
                print("Please Select a number from the list above")
                choice = -1
        except:
            choice = -1
            print("Input not recognised, please try again.")


    if choice == 1:
        get_related_chemicals()
    elif choice == 2:
        cluster()
    elif choice == 3:
        cluster_different_dataset()  
    elif choice == 4:
        smile_to_2D_structure()
    elif choice == 5:
        get_name_from_smile()



if __name__ == "__main__":
    while True:
        main()
        if not confirmation():
            break


# Issues, at some point during processing some chemicals are duplicated