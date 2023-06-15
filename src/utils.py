import numpy as np
import os
def levenshtein_distance(token1, token2):
    """
    Levenshtein distance is a metric used to quantify the difference or similarity between two strings.
    It measures the minimum number of single-character edits (insertions, deletions, or substitutions) required to transform one string into another.

    """
    distances = np.zeros((len(token1) + 1, len(token2) + 1))

    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1

    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2
        
    a = 0
    b = 0
    c = 0
    
    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if (token1[t1-1] == token2[t2-1]):
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]
                
                if (a <= b and a <= c):
                    distances[t1][t2] = a + 1
                elif (b <= a and b <= c):
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1

    return distances[len(token1)][len(token2)]


def linebreak():
    print("-"*20 + "\n")


def get_directory():
    # Gets the directory of the data folder, relative to position of this file
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def confirmation():
    ans = input("Do you wish to continue? Y/N: ")
    if ans.lower() == "y":
        return True
    
    elif ans.lower() == "n":
        print("Exiting...")
        return False
    else:
        print("Input not recognised, Exiting...")
        return False
    
def get_cluster_input():
    n_clusters = 0
    while n_clusters < 1:
        try:
            n_clusters = int(input(f"Enter Number of Clusters: "))
        except:
            print("Input not recognised, please try again.")

    return n_clusters
        
        